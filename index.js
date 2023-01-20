const express = require('express')
require('./db/connect')
const dotenv=require("dotenv")

const app=express()
dotenv.config()


//middlewares
app.use(express.json());


app.listen(process.env.PORT || 5000,()=>{
    console.log("Backend server is running")
})
