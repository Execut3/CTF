FROM node:lts AS runtime
WORKDIR /app

RUN npm install -g pnpm

COPY package.json .
COPY pnpm-lock.yaml .

RUN pnpm install

COPY quotes quotes
COPY app.js .

EXPOSE 3000
ENV PORT=3000
ENV NODE_ENV=production
CMD ["pnpm", "start"]
