<template>
  <form @submit="onSubmit" class="add-form">
      <div class="form-control">
        <label>search By title</label>
        <input type="text" v-model="title" name="title" placeholder="Tittle" />
      </div>
      <input type="submit" value="search" class="btn btn-block">
       <br>
      <hr>
      <hr>
 </form>    
    
</template>
<script>
export default{
    name:'Searchbook',
    data(){
        return {
            title:'',
        }
    },
    methods:{
        onSubmit(e){
        e.preventDefault();
        if(!this.title){
            alert('please add tittle')
            return
        }
        const sbook={
            title:this.title,
        }
        console.log(sbook);
        this.$emit('search-book',sbook)
        this.title=''
    },
},
}

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
  background-color: rgb(255, 255, 255);
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