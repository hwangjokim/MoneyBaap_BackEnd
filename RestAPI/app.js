const express = require("express");
const mysql = require("mysql2/promise");
const dotenv = require('dotenv');
dotenv.config();
const pool = mysql.createPool({
  user: process.env.DATABASE_USERNAME,
  host: "3.39.149.172",
  database: process.env.DATABASE_NAME,
  password: process.env.DATABASE_PASSWORD,
  port: 3306,
  connectionLimit: 100,
});

const app = express();
const port = 5921;

var cors = require("cors");
app.use(cors());

app.get("/places", async (req, res) => {
  const conn = await pool.getConnection();
  let [results] = await conn.query(
    "SELECT name, link, addr, star FROM place WHERE 1"
  );
  await conn.release();
  res.json({ places: results });
});

app.get("/lowPrice", async (req, res) => {
  const { search } = req.query;
  console.log("search ! => " + search);
  const conn = await pool.getConnection();
  let [results] = await conn.query(
    "SELECT p.name As placeName, p.link, p.addr, p.star, m.name, m.price, m.imgUrl \
                                        FROM place p \
                                        JOIN menu m \
                                            ON p.idx = m.placeIdx \
                                        WHERE m.name LIKE ? \
                                        ORDER BY m.price ASC",
    ["%" + search + "%"]
  );
  await conn.release();
  res.json({ menus: results });
});

app.listen(port, () => {
  console.log("start! express server");
});