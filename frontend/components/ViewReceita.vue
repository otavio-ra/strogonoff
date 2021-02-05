<template>
    <div>
        <!-- <usercard :user="user"></usercard> -->
        <!-- <timeline :posts="posts"></timeline> -->
        <v-list-tile avatar :key="post.id">
            <v-list-tile-avatar>
                <img :src="post.author_avatar">
            </v-list-tile-avatar>

            <v-list-tile-content>
                <v-list-tile-title>
                    <router-link :to="{name: 'receita'}"></router-link> /
                        {{post.prato}} /
                        <!-- {{tweet.author_username}} / -->
                        {{post.created_at | timeago}}
                </v-list-tile-title>
                <v-list-tile-sub-title>
                    {{post.prato}}
                    {{post.introducao}}
                    {{post.ingredientes}}
                    {{post.preparo}}
                </v-list-tile-sub-title>
            </v-list-tile-content>
        </v-list-tile>
    </div>
</template>

<script>
// import timeline from '~/components/Timeline.vue'
// import usercard from '~/components/UserCard.vue'

export default {
  props: ['user', 'post'],
//   components: {
//       timeline, usercard
//   },
  data (){
      return {
      }
  }
}
</script>

<style>
</style>