<script lang="ts" setup>
import axios from 'axios';
import {ref} from 'vue'
import { useRouter } from 'vue-router';
const router = useRouter()

const email = ref('')
const password = ref('')

async function submitForm(event: any) {
  const body = {email: email.value, password: password.value};
  try {
    event.preventDefault();
    const response = await axios.post("http://127.0.0.1:5000/register", body);
    email.value = '';
    password.value = '';
    if (response.status === 201) {router.push({path: 'Gallery'})}
  } catch (error) {
    console.error(error);
  }
}
</script>

<template>
  <form class="form-wrapper">
    <div class="email-wrapper">
      <div class="input-label">Enter your email</div>
      <input v-model="email" class="input-field input-field__email" type="email"/>
    </div>
    <div class="password-wrapper">
      <div class="input-label">Enter your password</div>
      <input v-model="password" class="input-field input-field__password" type="password"/>
    </div>
    <input class="input-submit form-btn button-item"
           type="submit" value="sign in" @click="submitForm"/>
  </form>
</template>

<style lang="scss" scoped>


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
