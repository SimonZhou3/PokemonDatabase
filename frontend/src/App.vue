<template>
  <div>
    <div id="nav">
      <trainer-nav-bar />
    </div>
    <router-view />
  </div>
</template>

<script>
import TrainerNavBar from "@/views/trainerNavBar";
export default {
  components: { TrainerNavBar },
};
</script>


<style>

</style>