<template>
    <form @submit="onSubmit" class="add-form">
      <div class="form-control">
        <label>Book : </label>
        <input type="text" v-model="title" name="Book" placeholder="Add Book" />
      </div>
      <div class="form-control">
        <label>auther : </label>
        <input
          type="text"
          v-model="auther"
          name="auther"
          placeholder="Add the auther"
        />
      </div>
      <div class="form-control">
        <label>image : </label>
        <input
          type="text"
          name="image"
          v-model="image"
          placeholder="Add image"
        />
      </div>
      <div class="form-control">
        <label>discription : </label>
        <input
          type="text"
          v-model="discription"
          name="discription"
          placeholder="Add discription"
        />
      </div>
      <div class="form-control">
        <label>publish_date: </label>
        <input
          type="text"
          name="publish_date"
          v-model="publish_date"
          placeholder="Add the published Date"
        />
      </div>
      <input type="submit" value="Save book" class="btn btn-block" />
      <br>
      <hr>
      <hr>
    </form>
  </template>
    
    <script>
  export default {
    name: "Addbook",
    data() {
      return {
        id: Math.floor(Math.random() * 10000),
        title: "",
        auther: "",
        image:"",
        discription: "",
        publish_date: "",
        // reminder: false,
      };
    },
    methods: {
      onSubmit(e) {
        e.preventDefault();
  
        if (!this.title) {
          alert("Please add a book");
          return;
        }
  
        const newbook = {
          title: this.title,
          auther: this.auther,
          image:this.image,
          discription: this.discription,
          publish_date: this.publish_date,
          
        };
  
        this.$emit("add-book", newbook);
  
        this.title = "";
        this.auther = "";
        this.image="";
        this.discription = "";
        this.publish_date = "";
        
      },
    },
  };
  </script>
  <style scoped>
  .add-form {
    margin-bottom: 40px;
  }
  
  .form-control {
    margin: 20px 0;
  }
  
  .form-control label {
    display: block;
        color: white;

  }
  
  .form-control input {
    width: 100%;
    height: 40px;
    margin: 5px;
    padding: 3px 7px;
    font-size: 17px;
     background-color: white;
    color: rgb(0, 0, 0);
    border: none;
    border-radius: 10px;
  }
  
  .form-control-check {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  
  .form-control-check label {
    flex: 1;
  }
  
  .form-control-check input {
    flex: 2;
    height: 20px;
   
  }
  </style>