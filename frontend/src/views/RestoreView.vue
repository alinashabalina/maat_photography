<script setup lang="ts">
import HeaderComponent from "@/components/HeaderComponent.vue";
import {type Ref, ref} from "vue";
const email = ref('')
const isDisabled = ref(false)
const modalData = ref("")
function restorePassword(event: Event): Ref<string> {
  event.preventDefault();
  fetch("http://127.0.0.1:5000/restore",
      {
        method: "POST", body: JSON.stringify({email: email.value})
      })
      .then((response) => response.json())
      .then((data) => {
        modalData.value = data["message"];
      })
      .catch((error) => {
        modalData.value = "Oops something went wrong. Try again later";
      })
  email.value = '';
  return modalData
}
</script>
<template>
  <HeaderComponent/>
  <div class="header">Restore password</div>
  <form class="form-wrapper">
    <div class="email-wrapper">
      <div class="input-label">Enter your email</div>
      <input v-model="email" class="input-field input-field__email" type="email"/>
    </div>
    <input :disabled="isDisabled" class="input-submit form-btn button-item"
           type="submit" value="restore" @click="restorePassword"/>
  </form>
</template>

<style lang="scss" scoped>
@use 'views';
@use '@/components/components';
@media only screen and (max-width: 600px) {
  .header {
    font-family: views.$primary-font;
    font-size: 40px;
    width: 99vw;
    text-align: center;
    margin-top: 10vh;
  }
  .form-wrapper {
    width: 60vw;
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

  .input-submit {
    margin-top: 30px;
    margin-left: auto;
    margin-right: auto;
    width: 60vw;
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
    width: 25vw;
    height: 20vh;
    margin-left: auto;
    margin-right: auto;
  }

  .email-wrapper {
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

  .form-btn {
    height: 5vh;
    width: 25vw;
    border: none;
    border-radius: 5px;
    font-family: views.$primary-font;
    font-weight: 500;
    background-color: components.$mid-grey;
    font-size: 18px;
    margin-right: auto;
    margin-left: auto;

    &:hover {
      background-color: #7d7d7f;
      transition: 1s;
    }
  }


}

@media only screen and (min-width: 1000px) {
  .form-wrapper {
    width: 30vw;
    height: 250px;
    margin-left: auto;
    margin-right: auto;
  }

  .email-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .input-submit {
    margin-top: 30px;
    width: 30vw;
    margin-left: auto;
    margin-right: auto;
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

