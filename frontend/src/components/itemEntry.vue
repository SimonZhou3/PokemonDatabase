<template>
    <div class="itemContainer" ref="itemContainer">
        <div class="itemData" id="desc"> {{this.$props.itemData.description}}</div>
        <div class="itemData" id="category"><b>category:</b> {{this.$props.itemData.category}}</div>
        <div class="itemData" id="cost"><b>cost:</b> {{this.$props.itemData.cost}}</div>
    </div>
</template>

<script>
export default {
    props:["itemData"],
    data() {
        return {
        }
    },
    // mounted() {
    //     this.accuracy = this.$props.acc
    // }
}
</script>

<style scoped>
.itemContainer {
    /* border: 1px solid orange; */
    width: 90%;
    display:flex;
    flex-direction: column;
    margin-left: auto;
    margin-right: auto;
}
.itemData{
    /* border: 1px solid blue; */
}
</style>