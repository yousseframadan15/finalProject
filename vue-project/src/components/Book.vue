<template>
  <div class="book">
    <h3>
      {{ book.title }}
      <i @click="onDelete(book.id)" class="fas fa-times"></i>
    </h3>
    <p>{{ book.author }}</p>
  </div>
</template>
<script>
export default {
  name: "Book",
  props: {
    book: Object,
  },
  methods:{
    onDelete(id){
        this.$emit('delete-book' , id)
    }

  }
};
</script>
<style scope>
.fas {
  color: red;
}

.book {
  background: #0e4e6b;
  margin: 5px;
  padding: 10px 20px;
  cursor: pointer;
}
.book:hover{
  background-color: darkgreen;
}


.book h3 {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
</style>