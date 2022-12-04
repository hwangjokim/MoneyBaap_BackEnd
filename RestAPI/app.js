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
app.use(cors());
const port = 5921;

app.get('/places/:school', async (req, res) => {
    let school = req.params.school;
    const conn = await pool.getConnection();
    let [results] = await conn.query("SELECT name, link, addr, star, distance FROM place WHERE school = ? ORDER BY distance ASC, star DESC",[school]);
    await conn.release();
    res.json({places: results});
})

app.get('/lowPrice/:school', async (req, res) => {
    let school = req.params.school;
    const { search } = req.query;
    const conn = await pool.getConnection();
    let [results] = await conn.query("SELECT p.name As placeName, p.link, p.addr, p.star, p.distance, m.name, m.price, m.imgUrl \
                                        FROM place p \
                                        JOIN menu m \
                                            ON p.idx = m.placeIdx \
                                        WHERE m.name LIKE ? \
                                        AND p.school = ? \
                                        ORDER BY m.price ASC, p.distance ASC", ["%" + search + "%", school]);
    await conn.release();
    res.json({menus: results});
})

app.listen(port, () => {
    console.log('start! express server');
})