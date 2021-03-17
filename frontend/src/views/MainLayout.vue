<template>
    <div>
        <v-navigation-drawer color="deep-purple darken-2" app v-model="drawer">
          <v-sheet color="grey lighten-4"
                   class="pa-4">
            <v-avatar
                color="blue"
                size="100">
                <span class="white--text">{{ currentUser }}</span>
            </v-avatar>
            <div class="pt-2">{{ currentUser }}</div>
          </v-sheet>

          <v-divider></v-divider>

          <v-list nav
                  dense
                  class="white--text">
            <v-list-item-group v-model="selectedItem"
                               color="white">
              <v-list-item v-for="(item, i) in items"
                           :key="i"
                           class="white--text"
                           @click="redirect(item.path)">
                <v-list-item-icon>
                  <v-icon color="white" v-text="item.icon"></v-icon>
                </v-list-item-icon>

                <v-list-item-content class="white--text">
                  <v-list-item-title v-text="item.text"></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-navigation-drawer>

        <v-app-bar class="white--text" color="deep-purple darken-4" app>
          <v-app-bar-nav-icon color="white" @click="drawer = !drawer"></v-app-bar-nav-icon>
          <div class="text-h6 pl-2" style="font-family: 'Playfair Display', serif;">
            Polaroid
          </div>
          <v-icon
            class="ml-2"
            large
            color="white">
            mdi-instagram
          </v-icon>
          <v-btn
            class="ma-2"
            outlined
            style="position: absolute; right: 4px"
            color="white"
            @click="logout()">
              Logout
          </v-btn>
        </v-app-bar>

        <!-- Sizes your content based upon application components -->
        <v-main>

          <!-- Provides the application the proper gutter -->
          <v-container fluid>

            <!-- If using vue-router -->
            <router-view></router-view>
          </v-container>
        </v-main>

        <v-footer color="deep-purple darken-4" app>
          <!-- -->
        </v-footer>
    </div>
</template>

<script>
export default {
  name: "MainLayout",
  mounted() {
    this.checkLoggedIn()
    this.loadUser()
  },
  data: () => ({
    drawer: null,
    selectedItem: null,
    currentUser: '',
    userFirstname: '',
    userLastname: '',
    items: [
      { id: 0, text: 'My Feed', path: '/feed', icon: 'mdi-view-list' },
      { id: 1, text: 'My Profile', path: '/myprofile', icon: 'mdi-account' },
      { id: 2, text: 'My Connections', path: '/connections', icon: 'mdi-account-multiple-plus' },
      { id: 3, text: 'Notifications', path: '/feed', icon: 'mdi-bell' },
      { id: 4, text: 'Settings', path: '/myprofile', icon: 'mdi-cog' }
    ]
  }),
  methods: {
    redirect(path){
      if(this.$router.history.current.path === path){
        return
      }
      this.$router.push(path)
    },
    loadUser(){
      this.currentUser = this.$session.get('current_user')
    },
    checkLoggedIn() {
      this.$session.start();
      if (!this.$session.has("token")) {
        this.$router.push('/');
      }
    },
    logout: function () {
      this.$session.destroy()
      this.$router.push('/')
    }
  }
};
</script>
