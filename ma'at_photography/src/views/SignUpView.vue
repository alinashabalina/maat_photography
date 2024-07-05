<script lang="ts" setup>
import axios from 'axios';
import {ref} from 'vue'
import HeaderComponent from "@/components/HeaderComponent.vue";

const email = ref('')
const password = ref('')
const name = ref('')

async function submitForm(event: any) {
  const body = {email: email.value, password: password.value};
  console.log(body);
  try {
    event.preventDefault();
    const response = await axios.post("http://127.0.0.1:5000/register", body);
    email.value = '';
    password.value = '';
    console.log(response)
  } catch (error) {
    console.error(error);
  }
}
</script>

<template>
  <HeaderComponent class="head"/>
  <div class="header">Join us</div>
  <form class="form-wrapper">
    <div class="email-wrapper">
      <div class="input-label">Enter your email</div>
      <input v-model="email" class="input-field input-field__email" type="email"/>
    </div>
    <div class="email-wrapper">
      <div class="input-label">Enter your name</div>
      <input v-model="name" class="input-field input-field__email" type="text"/>
    </div>
    <div class="email-wrapper">
      <div class="input-label">Enter your password</div>
      <input v-model="password" class="input-field input-field__email" type="password"/>
    </div>
    <div class="email-wrapper">
      <div class="input-label">Confirm your password</div>
      <input v-model="password" class="input-field input-field__email" type="password"/>
    </div>
    <input class="input-submit form-btn button-item"
           type="submit" value="sign in" @click="submitForm"/>
  </form>
</template>

<style lang="scss" scoped>
@use 'views';

@media only screen and (max-width: 600px) {
  .header {
    font-family: views.$primary-font;
    font-size: 40px;
    width: 99vw;
    text-align: center;
    margin-top: 10vh;
  }
  .form-wrapper {
    width: 50vh;
    height: 50vh;
    margin-left: auto;
    margin-right: auto;
    border-radius: 10px;
  }

  .email-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .password-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .input-submit {
    margin-top: 30px;
    margin-left: 30vw;
  }

  .input-label {
    margin-top: 20px;
    margin-bottom: 10px;
    text-align: center;
    font-size: 18px;
  }

  .input-field {
    width: 60vw;
    height: 6vh;
    border: none;
    border-radius: 10px;
  }

}

@media only screen and (min-width: 600px) {
  .header {
    font-family: views.$primary-font;
    font-size: 60px;
    width: 99vw;
    text-align: center;
    margin-top: 10vh;
  }

  .form-wrapper {
    width: 30vh;
    height: 20vh;
    margin-left: auto;
    margin-right: auto;
  }

  .email-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .password-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .input-submit {
    margin-top: 30px;
    margin-left: 9vw;
  }

  .input-label {
    margin-top: 20px;
    margin-bottom: 10px;
    text-align: center;
    font-size: 40px;
  }

  .input-field {
    width: 50vw;
    height: 4vh;
    border: none;
    border-radius: 10px;
  }

}

@media only screen and (min-width: 1000px) {

  .header {
    font-family: views.$primary-font;
    font-size: 80px;
    width: 99vw;
    text-align: center;
    margin-top: 10vh;
  }

  .form-wrapper {
    width: 500px;
    height: 250px;
    margin-left: auto;
    margin-right: auto;
  }

  .email-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .password-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .input-submit {
    margin-top: 30px;
    margin-left: 150px;
  }

  .input-label {
    margin-top: 20px;
    margin-bottom: 10px;
    text-align: center;
    font-size: 18px;
  }

  .input-field {
    width: 400px;
    height: 60px;
    border: none;
    border-radius: 10px;
  }
}
</style>
