<script setup lang="ts">
import axios from 'axios';
import { ref } from 'vue'
const email = ref('')
const password = ref('')
const isDisabled = ref(true)

async function submitForm(event:any) {
  const body = { email: email.value, password: password.value };
  console.log(body);
  isDisabled.value = true;
  if (body.email.length === 0 || body.password.length === 0) {isDisabled.value} else {isDisabled.value = false;}
  try {
    event.preventDefault();
    const response = await axios.post("https://reqres.in/api/articles", body);
    email.value = '';
    password.value = '';
    console.log(response)}
  catch (error) {
    console.error(error);
  }
}
</script>

<template>
  <form class="form-wrapper" >
    <div class="email-wrapper">
      <div class="input-label">Enter your email</div>
      <input type="email" class="input-field input-field__email" v-model="email"/>
    </div>
    <div class="password-wrapper">
      <div class="input-label">Enter your password</div>
      <input type="password" class="input-field input-field__password" v-model="password"/>
    </div>
    <input type="submit" class="input-submit form-btn button-item"
    value="sign in" @click="submitForm" :disabled="isDisabled"/>
  </form>
</template>

<style scoped lang="scss">


@media only screen and (max-width: 600px) {

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
  margin-left: 15vw;
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
