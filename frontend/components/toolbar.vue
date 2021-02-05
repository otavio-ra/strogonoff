<template>
  <v-toolbar class="toolbar" color="#bb4b00" dark fixed app clipped-right>
    <v-toolbar-title>
      <v-btn class=botao_toolbar flat :to="{name: 'index'}"><v-icon class="icon">home</v-icon></v-btn>
    </v-toolbar-title>
    <v-spacer class="titulo">Strogonoff de todo Dia</v-spacer>
    <v-btn class="botao_toolbar" flat dark ripple @click="open_button($event)"><strong>Add</strong><v-icon>add</v-icon></v-btn>
    

    <!-- #######################################################################
             SEÇÃO LOGIN A SER INTEGRADA COM BACKEND POSTERIORMENTE
         ####################################################################### -->

    <!-- <v-btn v-if="!logged_user" flat dark ripple class="ma-0 ml-5"  @click="open_login_dialog($event)">Login</v-btn>
    <v-menu v-if="logged_user" offset-y>
      <v-btn icon slot="activator" class="ma-0 ml-5">
        <v-avatar size="36px">
          <img src="https://graph.facebook.com/4/picture?width=300&height=300">
        </v-avatar>
      </v-btn>
      <v-card class="no-padding">
        <v-list two-line>
          <v-list-tile avatar>
            <v-list-tile-avatar>
              <v-avatar>
                <img src="https://graph.facebook.com/4/picture?width=300&height=300">
              </v-avatar>
            </v-list-tile-avatar>
            <v-list-tile-content>
              <v-list-tile-title>{{logged_user.first_name}} {{logged_user.last_name}}</v-list-tile-title>
              <v-list-tile-sub-title>{{logged_user.email}}</v-list-tile-sub-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
        <v-divider></v-divider>
        <v-list>
          <v-list-tile @click="switchMode()">
            <v-list-tile-content>
              <v-list-tile-title>Staff mode</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
          <v-list-tile @click="logout()">
            <v-list-tile-content>
              <v-list-tile-title>Log out</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-card>
    </v-menu> -->


    <createReceita ref="createReceita"/>
    <login-dialog ref="login_dialog"/>
  </v-toolbar>
</template>

<script>
  import Vuex from 'vuex'
  import loginDialog from '~/components/login-dialog.vue'
  import createReceita from '~/components/createReceita.vue'
  import Snacks from '~/helpers/Snacks.js'
  import AppApi from '~apijs'
  
  export default {
    data () {
      return{
        visible: false
      }
    },
    components: {
      loginDialog,
      createReceita
    },
    computed: Object.assign(
      {},
      Vuex.mapGetters([
        'logged_user'
      ])
    ),
    props: ['state'],
    methods: {
      open_login_dialog (evt) {
        this.$refs.login_dialog.open();
        evt.stopPropagation();
      },
      logout(){
        AppApi.logout().then(()=>{
          this.$store.commit('SET_LOGGED_USER', null);
          Snacks.show(this.$store, {text: 'Até logo!'})
        });
      },
      open_button (clique) {
        this.$refs.createReceita.open();
        clique.stopPropagation();
      },
      close () {
        this.visible = false;
      },
      open () {
        this.visible = true;
      }
    }
  }
</script>

<style>
  @import url('https://fonts.googleapis.com/css?family=Sofia');

  .icon {
    margin: 10px;
  }
  .toolbar {
    align-content: center;
    justify-content: center;
  }
  .titulo {
    font-family: "Sofia", sans-serif;
    font-size: 200%;
  }
  .botao_toolbar {
    font-weight: bold;
    border-radius: 20px;
  }

  @media only screen and (max-width: 650px) {
    .titulo{
      font-size: 100%;
    }
  }
</style>