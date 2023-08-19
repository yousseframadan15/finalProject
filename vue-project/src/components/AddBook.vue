<template>
  <form @submit="onSubmit" class="add-form">
    <div class="form-control">
      <label>Book : </label>
      <input type="text" v-model="title" name="title" placeholder="Add Book" />
    </div>
     <div class="form-control">
      <label>auther : </label>
      <input
        type="text"
        name="auther"
        v-model="auther"
        placeholder="Add auther"
      />
    </div>
    <div class="form-control">
      <label>image : </label>
      <input
        type="text"
        v-model="image"
        name="image"
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
      <label>publish_date : </label>
      <input
        type="text"
        v-model="publish_date"
        name="publish_date"
        placeholder="Add the Published date"
      />
    </div>
    <input style="color:white; background-color:darkgreen;" type="submit" value="Save book" class="btn btn-block" />
  </form>
  <hr>
  <br>
</template>
  
  <script>
export default {
  name: "Addbook",
  data() {
    return {
      id: Math.floor(Math.random() * 10000),
      title: "",
      image:"",
      auther: "",
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
        //   reminder: this.reminder,
      };

      this.$emit("add-book", newbook);

      this.title = "";
      this.auther = "";
      this.image = "";
      this.discription = "";
      this.publish_date = "";
      // this.reminder = false
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
  display: inline;
}

.form-control input {
  width: 97%;
  height: 30px;
  margin: 5px;
  padding: 3px 7px;
  font-size: 15px;
  display: inline-table;
  color: rgb(0, 0, 0);
}

.form-control-check {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.form-control-check label {
  flex: 1;
  text-align: center;
}

.form-control-check input {
  flex: 2;
  height: 20px;
}
</style>