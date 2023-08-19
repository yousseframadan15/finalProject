<template>
  <header>
    <h1 style="color:white;">{{ title }}</h1>
    <Button
      @btn-click="$emit('toggle-add-book')"
      :text="showAddBook ? 'Close' : 'Add Book'"
      :color="showAddBook ? 'red' : '#13693e'"
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
    color: rgb(16, 185, 30);
}
</style>