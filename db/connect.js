const dotenv = require('dotenv');
const mongoose=require('mongoose')

dotenv.config()
mongoose.connect(
    process.env.MONGO_URL,{
      useNewUrlParser: true,
      useUnifiedTopology: true
  }
    ).then(
        ()=> console.log("db succefully connected")
        ).catch(
            (err)=>{console.log("error occured",err)}
        )
  
  mongoose.connection.on("disconnected", () => {
    console.log("mongoDB disconnected!");
  });