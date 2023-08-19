<template>
  <header>
    <h1>{{ title }}</h1>
    <Button
      @btn-click="$emit('toggle-add-book')"
      :text="showAddBook ? 'Close' : 'Add Book'"
      :color="showAddBook ? 'red' : 'green'"
    class="bot"
    />
  </header>
</template>
<script>
import Button from "./Button.vue";
export default {
  name: "Header",
  props: {
    title: String,
    showAddBook: Boolean,
  },
  components: {
    Button,
  },
};
</script>
<style scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}
.bot:hover{
    color: rgb(0, 0, 0);
}
</style>