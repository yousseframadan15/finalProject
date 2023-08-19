<template>
  <div :key="book.id" v-for="book in books">
    <Book @delete-book="$emit('delete-book', book.id)" :book="book" />
    <button class="btn" @click="updateBook(book)">Edit</button>
    <button class="btn" @click="deleteBook(book.id)">Delete</button>
  </div>
</template>
<script>
import Book from "./Book.vue";
// import editBook from "./EditBook.vue"
export default {
//   name: "Books",
  props: {
    books: Array,
    editBook: Function,
  },
  methods: {
    async deleteBook(id) {
      if (confirm("Are you sure?")) {
        const res = await fetch(`http://127.0.0.1:8000/books/${id}`, {
          method: "DELETE",
        });
        res.status === 204
          ? (this.books = this.books.filter((book) => book.id !== id))
          : alert("Error in deleting book");
      }
    },
      async updateBook(updatedBook) {
      try {
        const response = await fetch(`http://localhost:8000/books/${updatedBook.id}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(updatedBook),
        });

        if (response.status === 200) {
          const index = this.books.findIndex(book => book.id === updatedBook.id);
          if (index !== -1) {
            this.books[index] = updatedBook;
          }
        } else {
          alert('Error updating book');
        }
      } catch (error) {
        console.error('Error updating book:', error);
        alert('An error occurred while updating the book.');
      }
      },
  },
  components: {
    Book,
  },
  emits: ["delete-book"],
  emits: ["edit-book"],
};
</script>

<style scoped>
button{
    background-color: rgb(39, 14, 5);
    
}
button:hover{
    background-color: rgb(71, 29, 14);
}
button:active{
    background-color: rgb(0, 0, 0);
}
</style>