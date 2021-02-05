<template>
  <div>
    <h1>{{receita}}</h1>
  </div>
</template>

<script>


export default {
  asyncData (context) {
    return {
      receita: context.params.receita
    }
  },
  data () {
    return {
    }
  }
}
</script>

<style>
</style>