import express from "express";
import jwt from "jsonwebtoken";
import path from "path";
import fs from "fs";

const SECRET_KEY = process.env.SECRET_KEY || "secret";
const COOKIE_NAME = "quotes-auth";

const FREE_TIER_QUOTE_LIMIT = 5;

const app = express();

app.get("/quote", (req, res) => {
  const { id, random } = req.query;
  const { cookie } = req.headers;

  if (!cookie) {
    res.status(401);
    res.send({ error: "Not authenticated" });
    return;
  }

  const cookies = cookie.split(";").reduce((acc, cookie) => {
    const [key, value] = cookie.split("=").map((c) => c.trim());
    acc[key] = value;
    return acc;
  }, {});

  const cookieToken = cookies[COOKIE_NAME];

  if (!cookieToken) {
    res.status(401);
    res.send({ error: "Not authenticated" });
    return;
  }

  let decoded;
  try {
    decoded = jwt.verify(cookieToken, SECRET_KEY);
  } catch (e) {
    res.status(403);
    res.send({ error: "Invalid token" });
    return;
  }

  const filepath = path.resolve("./quotes");
  const quotes = fs.readFileSync(filepath, "utf-8").split("\n");

  if (random && random === "true") {
    const i = Math.floor(Math.random() * FREE_TIER_QUOTE_LIMIT);

    if (!decoded.subscribed && i >= FREE_TIER_QUOTE_LIMIT) {
      res.status(500);
      res.send({ error: "Not a paying subscriber" });
      return;
    }

    const quote = quotes[i];

    res.status(200);
    res.send({ quote, id: i });
    return;
  }

  if (id) {
    const i = Number(id);

    if (!decoded.subscribed && i >= FREE_TIER_QUOTE_LIMIT) {
      res.status(500);
      res.send({ error: "Not a paying subscriber" });
      return;
    }

    if (i < 0 || i >= quotes.length) {
      res.status(500);
      res.send({ error: "Invalid quote ID" });
      return;
    }

    const quote = quotes[parseInt(i)];

    res.status(200);
    res.send({ quote, id: i });
    return;
  }

  res.status(500);
  res.send({ error: "Unable to get quote" });
});

app.get("/register", (req, res) => {
  const token = jwt.sign(
    {
      subscribed: false,
    },
    SECRET_KEY,
    { expiresIn: "1h" }
  );

  res.cookie(COOKIE_NAME, token, {
    httpOnly: true,
    secure: true,
    maxAge: 3600000,
  });
  res.status(200);
  res.send({ message: "Signed in!" });
});

app.listen(process.env.PORT || 3000);
