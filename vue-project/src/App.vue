<template>
  <div class="container">
    <Header 
    @toggle-add-book="toggleAddBook"
     @toggle-edit-book="toggleeditBook"
      title="Library"
      :showAddBook="showAddBook"
      :showeditBook="showeditBook"

    />
    <div v-show="showAddBook">
      <AddBook @add-book="AddBook" />
    </div>
     <div v-show="showEditBook">
      <EditBook :book="selectedBook" />
    </div>
    <Books @delete-book="deleteBook" :books="books" :edit-book="editBook"  />

  </div>
</template>

<script>
import Header from "./components/Header.vue";
import AddBook from "./components/AddBook.vue";
import Books from "./components/Books.vue";
import EditBook from "./components/EditBook.vue";
export default {
  name: "App",
  components: {
    Header,
    Books,
    AddBook,
    EditBook
  },
  data() {
    return {
      books: [],
      showAddBook: false,
      selectedBook: null,
      showEditBook:false
    };
  },
  methods: {
     editBook(book) {
    this.selectedBook = book;
    this.showEditBook = true;
  },
    toggleAddBook(){
      this.showAddBook= !this.showAddBook
    },
    toggleeditBook(){
      this.showeditBook= !this.showeditBook
    },
     async AddBook(book) {
      const res =await fetch('http://127.0.0.1:8000/books',{
        method:"POST",
        headers:{
          'content-type':'application/json',
        },
        body:JSON.stringify(book),
      })
      console.log(res)
      const data =await res.json()
      this.books = [...this.books, data];
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
     async deleteBook(id) {
      if (confirm("Are you sure?")) {
        const res=await fetch(`http://127.0.0.1:8000/books/${id}`,{
          method:'DELETE'
        })
        res.status===204 ?(this.books = this.books.filter((book) => book.id !== id)):alert('Error in deleting book')
      }
    },
   async fetchBooks(){
        const res =await fetch('http://127.0.0.1:8000/books')
        const data =await res.json()
        return data
    },
    async fetchBook(id){
        const res =await fetch(`http://127.0.0.1:8000/books/${id}`)
        const data =await res.json()
        return data
    },
  },
   async created() {
    this.books = await this.fetchBooks()
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap');

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Poppins', sans-serif;
}

.container {
  max-width: 90%;
  margin: 30px auto;
  overflow: auto;
  min-height: 300px;
  border: 2px solid steelblue;
  padding: 30px;
  border-radius: 5px;
}

.btn {
  display: inline-block;
  background: #271a63;
  color: #fff;
  border: none;
  padding: 10px 20px;
  margin: 5px;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  font-size: 15px;
  font-family: inherit;
}

.btn:focus {
  outline: none;
}

.btn:active {
  transform: scale(0.98);
}

.btn-block {
  display: block;
  width: 100%;
}
</style>