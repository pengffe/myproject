<template>
  <div class = "home">
    <div class="signIn">
      <form>
        <input type="text" v-model="UserName" name="Email" placeholder="Email" style="width: 200px"></input>
        <input type="password" v-model="Password" name="Password" placeholder="Password" style="width: 200px"></input>
        <input type="submit" value="Log in" @click="" style="width: 100px"></input>
      </form>
    </div>
    <div class = "column1">
      <img src="../assets/oo.jpg" width="700" height="600" style="position: relative; left: -70px; top: 50px" >
    </div>
    <div class = "column2">
      <h2 style="text-align: left; font-size: 44px; margin-bottom: 20px">Welcome!</h2>
      <h2 style="text-align: left; font-size: 28px; margin-bottom: 60px; line-height: 1.2">Every day, enjoy your communication</h2>
      <form>
        <input type="text" v-model="UserName" name="Email" placeholder="Email"></input><br>
        <input type="password" v-model="Password" name="Password" placeholder="Password"></input><br>
        <select name="countries">
          <option value="+86">+86</option>
          <option value="+61">+61</option>
        </select>
        <input type="text" v-model="PhoneNumber" name="phoneNumber" placeholder="Phone number" style="width: 55%"></input><br>
        <lable style="font-size: smaller; position: relative; left: -80px">You can find your password by using the phone number</lable>
        <input type="submit" value="Sign up now" @click="user_register()"></input>
      </form>
<!--      <p style="font-size: smaller;">Copyright@</p>-->
    </div>
  </div>
</template>

<script>
    export default {
        name: "Registration",
        data() {
            return {
                UserName: '',
                Password: '',
                PhoneNumber:''
            }
        },
        mounted:
             function() {
                this.user_register()
             },
        methods: {
            user_register(){
                alert(this.UserName)
                this.$http.get('http://127.0.0.1:8000/api/user_register?user_name=' + this.UserName +
                    '&' + 'password=' + this.Password)
                    .then((response) =>{
                    var res = JSON.parse(response.bodyText)
                    if (res.error_num === 0) {
                        this.showBooks()
                    } else {
                        this.$message.error('新增书籍失败，请重试')
                        console.log(res['msg'])
                    }
                })
            }
        }
    }
</script>

<style scoped>
  h1{
    padding-bottom: 50px;
  }
  input[type=text], input[type=password] {
    width: 80%;
    padding: 18px 20px;
    margin: 20px 0px;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    font-size: larger;
  }
  select{
    width: 25%;
    height: 150%;
    padding: 18px 20px;
    margin: 20px 0px;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    font-size: large;
  }
  input[type=submit] {
    width: 80%;
    /*background-color: #4CAF50;*/
    background-color: #0033ff;
    color: white;
    padding: 18px 20px;
    margin: 20px 0;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: larger;
  }
  .column2 form{
    position: relative;
    left: -62px;
  }
  .signIn form{
    position: relative;
    right: 0px;
    padding: 0;
    border: 0;
  }
  p {
    text-align: left;
  }
  .column1{
    float: left;
    width: 40%;
  }
  .column2{
    float: right;
    /*background-color: #f1f1f1;*/
    width: 50%;
    padding-top: 30px;
    padding-bottom: 30px;
  }
  .signIn{
    background-color: #f1f1f1;
    width: 100%;
    /*padding-top: 5px;*/
    /*padding-bottom: 5px;*/
  }

</style>
