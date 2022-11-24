<template>
  <button class="entry" ref="entry" @click="queryTrainer">
    {{ this.$props.trainer.name }}
  </button>
</template>

<script>
export default {
  props: ["trainer"],
  data() {
    return {};
  },
  updated() {
  },
  methods: {
    queryTrainer() {
      this.$emit("querying", this.$props.trainer.trainer_id);
    },

    onResponseSpecific(genericData, versionData) {
      this.$emit("response", genericData, versionData)
    },
    async onResponse(dataGeneric) {
      console.log("received data from backend");
      let versions = dataGeneric.data[0].version_list;
      let filteredVersion = this.filterVersions(versions)
      this.$emit("response", dataGeneric, filteredVersion)

    },
  }
}

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
  background-color: #cf4444;
  cursor: pointer;
}
</style>