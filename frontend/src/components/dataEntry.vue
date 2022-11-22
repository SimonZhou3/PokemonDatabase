<template>
  <button class="entry" ref="entry" @click="queryData">
    {{ this.$props.data.name}}
  </button>
</template>

<script>
export default {
  props: ["data", "color"],
  data() {
    return {
        accentColor: this.$props.color,
    };
  },
  updated() {},
  methods: {
    queryData() {
        console.log("querying " +this.$props.data.name)
    }
  },
};
</script>

<style scoped>
.entry {
  height: 5vh;
  background-color: #ffffff00;
  margin-bottom: 1vh;
  width: 95%;
  border-radius: 2.5vh;
  border: 0;
  transition: background-color 0.3s;
  font-weight: bold;
}
.entry:hover {
    cursor: pointer;
  background-color: v-bind(accentColor);
}
</style>