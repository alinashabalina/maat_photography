<script setup lang="ts">
defineProps<{
  isShown: Boolean
}>()
import CloseButtonComponent from '@/components/shared/CloseButtonComponent.vue'
</script>

<template>
  <Transition name="modal">
    <div v-if="isShown" class="modal-screen">
      <div class="modal-container">
        <div class="modal-container__header">
          <slot name="header">register or sign in</slot>
        </div>
        <div class="modal-container__body">
          <slot name="body">blah blaf fields</slot>
        </div>
        <div class="modal-container__footer">
          <slot name="footer"
            >blah blah
            <CloseButtonComponent class="modal-container__button" @click="$emit('close')" />
          </slot>
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
  width: 400px;
  height: 200px;
  margin: auto;
  padding: 20px 30px;
  background-color: #f2efe5;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
}
</style>
