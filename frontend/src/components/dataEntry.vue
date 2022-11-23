<template>
  <button class="entry" ref="entry" @click="queryData">
    {{ this.dataName }}
  </button>
</template>

<script>
export default {
  props: ["data", "color", "type"],
  data() {
    return {
      accentColor: this.$props.color,
      dataName: null,
    };
  },
  updated() {},
  mounted() {
    // console.log(this.$props.data, this.$props.type)
    switch (this.$props.type) {
      case "Move":
        this.dataName = this.$props.data.name;
        break;
      case "Area":
        this.dataName = this.$props.data.area_name;
        break;
      case "Item":
        break;

      default:
        break;
    }
  },
  methods: {
    queryData() {
      console.log("querying " + this.dataName);
    },
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