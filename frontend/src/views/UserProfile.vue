<template>
    <v-container grid-list-sm>
      <v-layout row wrap align-center justify-center fill-height>
        <v-flex xs12 sm12 lg12 md12>
          <v-card class="mx-12 mt-2">
            <v-card-title class="black--text pl-4">
              <v-avatar
                color="blue"
                size="100">
                <span class="white--text">USER</span>
              </v-avatar>
              <div>
                <div class="pb-2">
                  <span class="text-h5 headline px-4" align="left">Firstname Lastname</span>
                  <v-btn class="white--text text-capitalize mx-2"
                        small
                        rounded
                        color="blue"
                        @click="follow()">
                    Follow
                  </v-btn>
                  <v-btn class="white--text text-capitalize"
                        small
                        rounded
                        outlined
                        color="blue"
                        @click="logout()">
                    Unfollow
                  </v-btn>
                </div>
                  <span class="subtitle-2 pl-4" align="left">Followers: 0</span>
                  <span class="subtitle-2 pl-4" align="left">Following: 0</span>
              </div>
            </v-card-title>

            <v-divider class="mt-1 mb-3"></v-divider>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col
                    v-for="n in 9"
                    :key="n"
                    class="d-flex child-flex"
                    cols="4">
                    <v-img
                      :src="`https://picsum.photos/500/300?image=${n * 5 + 10}`"
                      :lazy-src="`https://picsum.photos/10/6?image=${n * 5 + 10}`"
                      aspect-ratio="1"
                      class="grey lighten-2">
                      <template v-slot:placeholder>
                        <v-row
                          class="fill-height ma-0"
                          align="center"
                          justify="center">
                          <v-progress-circular
                            indeterminate
                            color="grey lighten-5"
                          ></v-progress-circular>
                        </v-row>
                      </template>
                    </v-img>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
          </v-card>

          <NewPostDialog :showDialog="showPostDialog"
                         @cancelClicked="showPostDialog = false"/>

        </v-flex>
      </v-layout>
    </v-container>
</template>

<script>
import NewPostDialog from '../components/NewPostDialog'
// import axios from 'axios';
export default {
  name: 'MyProfile',
  components: {
    NewPostDialog
  },
  data: () => ({
      loading: false,
      snackbarError: false,
      errorMessage: 'Unable to post!',
      snackbarApproved: false,
      approvedMessage: 'New post successfully created!',
      timeout: 5000,
      showPostDialog: false,
      allUsers: null
  }),
  methods: {
    follow() {
      // this.loading = true;
      // axios.get('http://localhost:8000/api-auth/user/getAll').then(response => {
      //   this.allUsers = response.data
      //   console.log(this.allUsers)
      //   this.snackbarApproved = true
      // }).catch(e => {
      //   this.snackbarError = true
      //   this.loading = false
      //   console.log(e)
      // })
    },
    newPost() {
      this.showPostDialog = true
    }
  },
  computed: {
  }
}
</script>
