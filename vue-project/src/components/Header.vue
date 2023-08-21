<template>
    <header>
      <h1>{{ title }}</h1>
      <Button
        @btn-click="$emit('toggle-add-book')"
        :text="showAddBook ? 'Close' : 'Add Book'"
        :color="showAddBook ? 'red' : 'green'"
      />
      <Button
        @toggle-search-book="$emit('toggle-search-book')"
        :text="showAddsearch ? 'Close' : 'search'"
        :color="showAddsearch ? 'red' : 'yellow'"
      />
      <Button
        @toggle-update-book="$emit('toggle-update-book')"
        :text="showupdatebook ? 'Close' : 'update'"
        :color="showupdatebook ? 'red' : 'blue'"
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
      showAddsearch:Boolean,
      showupdatebook:Boolean,
    },
    components: {
      Button,
    },
  };
  </script>
<style scoped>
header{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    color:white;
}
</style>