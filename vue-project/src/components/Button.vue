<template>
    <button @click="onClick()" :style="{background:color}" class="btn">{{text}}</button>
    </template>
    <script>
    export default{
        name:'Button',
        props:{
            text:String,
            color:String,
        },
        methods:{
            onClick(){
                this.$emit('btn-click')
                this.$emit('toggle-search-book')
                this.$emit('toggle-update-book')
            }
    
        }
    }
    
    </script>