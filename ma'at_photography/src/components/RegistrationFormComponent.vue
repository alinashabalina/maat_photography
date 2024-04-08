<script setup lang="ts">
  const submitForm = () => {console.log('opop')}
</script>

<template>
  <form class="form-wrapper">
    <div class="email-wrapper">
      <div class="input-label">Enter your email</div>
      <input type="email" class="input-field input-field__email" />
    </div>
    <div class="password-wrapper">
      <div class="input-label">Enter your password</div>
      <input type="password" class="input-field input-field__password" />
    </div>
    <input type="submit" class="input-submit form-btn button-item"
    value="sign in" @click="submitForm"/>
  </form>
</template>

<style scoped lang="scss">
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
</style>
