<template>
    <div>
        <usercard :user="user"></usercard>
        <!-- <timeline :tweets="tweets"></timeline> -->
        <timeline :posts="posts"></timeline>
    </div>
</template>

<script>
import timeline from '~/components/Timeline.vue'
import usercard from '~/components/UserCard.vue'

export default {
//   props: ['user', 'tweets'],
  props: ['user', 'posts'],
  components: {
      timeline, usercard
  },
  data (){

  }
}
</script>

<style>
</style>