<script setup lang="ts"></script>

<template>
  <form class="form-wrapper">
    <div class="input-label">Enter your email</div>
    <input type="email" class="input-field input-field__email" />
    <div class="input-label">Enter your password</div>
    <input type="password" class="input-field input-field__password" />
    <input type="submit-btn" class="input-submit" value="sign in" />
  </form>
</template>

<style scoped lang="scss">
.form-wrapper {
  width: 500px;
  height: 250px;
  margin-left: auto;
  margin-right: auto;
  border: 1px solid black;
}

.password {
  margin-left: 100px;
}
</style>
