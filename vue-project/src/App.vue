<template>
  <div class="container">
    <Header @toggle-add-book="toggleAddBook"
      title="Library"
      :showAddBook="showAddBook"

    />
    <div v-show="showAddBook">
      <AddBook @add-book="AddBook" />
    </div>
    <Books @delete-book="deleteBook" :books="books" />
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import AddBook from "./components/AddBook.vue";
import Books from "./components/Books.vue";
export default {
  name: "App",
  components: {
    Header,
    Books,
    AddBook,
  },
  data() {
    return {
      books: [],
      showAddBook: false,
    };
  },
  methods: {
    toggleAddBook(){
      this.showAddBook= !this.showAddBook
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
     async deleteBook(id) {
      if (confirm("Are you sure?")) {
        const res=await fetch(`http://127.0.0.1:8000/books/${id}`,{
          method:'DELETE'
        })
        res.status===200 ?(this.books = this.books.filter((book) => book.id !== id)):alert('Error in deleting book')
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
  max-width: 500px;
  margin: 30px auto;
  overflow: auto;
  min-height: 300px;
  border: 1px solid steelblue;
  padding: 30px;
  border-radius: 5px;
}

.btn {
  display: inline-block;
  background: #000;
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