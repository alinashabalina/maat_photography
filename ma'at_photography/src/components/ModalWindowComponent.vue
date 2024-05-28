<script setup lang="ts">
defineProps<{
  isShown: Boolean
  header: String
  close: Boolean
}>()
import RegistrationFormComponent from '@/components/RegistrationFormComponent.vue'
import FormButtonComponent from '@/components/shared/FormButtonComponent.vue'
import CloseButtonComponent from '@/components/shared/CloseButtonComponent.vue'
</script>

<template>
  <Transition name="modal">
    <div v-if="isShown" class="modal-screen">
      <div class="modal-container">
        <div class="modal-container__exit-button">
          <CloseButtonComponent @click="$emit('close')"/>
        </div>
        <div class="modal-container__no-exit">
        <div class="modal-container__header">
          {{ header }}
        </div>
        <div class="modal-container__body">
          <slot>
            <RegistrationFormComponent></RegistrationFormComponent>
            <div class="button-container">

              <FormButtonComponent
                class="button-item button-sign"
                action="sign up"
              ></FormButtonComponent>
              <FormButtonComponent
                class="button-item button-restore"
                action="forgot my password"
              ></FormButtonComponent>
            </div>
          </slot>
        </div>
      </div>
    </div>
    </div>
  </Transition>
</template>

<style lang="scss">
.modal-screen {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
}

.modal-container {
  width: 500px;
  height: 550px;
  margin: auto;
  padding: 20px 30px;
  background-color: #f2efe5;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  position: relative;

  &__body {
    width: inherit;
  }

  &__no-exit {
    margin-top: 10%;
  }

  &__header {
    text-align: center;
    font-family: 'Cinzel', serif;
    font-size: 40px;
  }

  &__exit-button {
    position: absolute;
    right: 15px;
    top: 10px;
  }

}

.button-container {
  margin-top: 20%;
  margin-left: auto;
  margin-right: auto;
  display: flex;
  width: 450px;
  justify-content: space-between;
}
</style>
