<template>
  <div class="book">
    <h3>
      Book title : {{ book.title }}
      <br>
      Book Auther : {{ book.auther }}
      <br>
      Book ID : {{ book.id }}
      <i @click="onDelete(book.id)" class="fas fa-times"></i>
    </h3>
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
  background: rgba(17,102,88,.7);
  margin: 5px;
  padding: 10px 20px;
  cursor: pointer;
  color: white;
   border: none;
    border-radius: 5px;
}
.book:hover{
  background-color: gray;
}

.book.reminder {
  border-left: 5px solid green;
}

.book h3 {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
</style>