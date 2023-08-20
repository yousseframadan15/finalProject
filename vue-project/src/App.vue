<template>
  <div class="container">
    <Header @toggle-update-book="toggleUpdatebook"
    @toggle-search-book="toggleAddsearch" 
     @toggle-add-book="toggleAddBook"
      title="Library"
      :showAddBook="showAddBook"
      :showAddsearch="showAddsearch"
      :showupdatebook="showupdatebook"
    />
    <div v-show="showAddBook">
      <AddBook @add-book="AddBook" />
      
    </div>
    <div v-show="showAddsearch">
      <Searchbook @search-book="searchBook"/>
      <Book  :book="book"/>
    </div>
    <div v-show="showupdatebook">
      <UpdateBook @update-book="updateBook"/>
    </div>
   <Books @delete-book="deleteBook" :books="books" />
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import AddBook from "./components/AddBook.vue";
import Books from "./components/Books.vue";
import Searchbook from "./components/Searchbook.vue";
import Book from "./components/Book.vue";
import UpdateBook from "./components/UpdateBook.vue";
export default {
  name: "App",
  components: {
    Header,
    Books,
    AddBook,
    Searchbook,
    Book,
    UpdateBook,
  },
  data() {
    return {
      books: [],
      showAddBook: false,
      book:{},
      showAddsearch:false,
      searched:false,
      showupdatebook:false,
    };
  },
  methods: {
    
    async searchBook(title){
      console.log(title.title)
       const res = await fetch(`http://127.0.0.1:8000/books/${title.title}`)
       const data =await res.json()
       this.book=data

    },
    toggleUpdatebook(){
      this.showupdatebook=!this.showupdatebook
    },
    toggleAddsearch(){
      this.showAddsearch=!this.showAddsearch
    },
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
        res.status===204 ?(this.books = this.books.filter((book) => book.id !== id)):alert('Error in deleting book')
      }
    },
   async fetchBooks(){
        const res =await fetch('http://127.0.0.1:8000/books')
        const data =await res.json()
        return data
    },
    async updateBook(listy){
        let id=listy[0];
        let booke=listy[1];
        const res =await fetch(`http://127.0.0.1:8000/books/${id}`,{
        method:"PUT",
        headers:{
          'content-type':'application/json',
        },
        body:JSON.stringify(booke),
      })
      console.log(res)
      this.books =await this.fetchBooks()
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
  background: #116658;
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
