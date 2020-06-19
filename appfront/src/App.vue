<template>
  <div id="app">
<!--    <div>-->
<!--      <router-link to="/Home" style="display: none">Home</router-link>-->
<!--      <router-link to="/Registration" style="display: none">Registration</router-link>-->
<!--    </div>-->
    <div>
          <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
</style>
