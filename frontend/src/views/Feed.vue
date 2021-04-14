<template>
    <v-container grid-list-md>
      <v-layout row wrap align-center justify-center fill-height>
        <v-flex xs12 sm8 lg5 md6>
                <v-card rounded outlined style="max-width: 800px">
                    <v-card-title>
                        Welcome to Polaroid, {{ currentUser }}!
                    </v-card-title>
                    <!-- <div class="px-3">
                      <v-text-field class="questrial no-top-padding" background-color="grey lighten-3" height="44px" rounded placeholder="Search a user"/>
                    </div> -->
                    <div v-for="post in feedPosts"
                    :key="post.id">
                    <v-divider class="mt-1 mb-1"></v-divider>
                    <v-card-title>{{ post.owner.username }}</v-card-title>
                    <div class="px-4">
                      <v-img
                        :src="post.picture"
                        :lazy-src="post.picture"
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
                    </div>
                    <div class="px-4 pb-2">
                      <strong>{{ post.owner.username }}</strong> - {{ post.description }}
                    </div>
                    <div class="px-4">
                      <v-textarea
                        label="Add comment..."
                        auto-grow
                        v-model="post.content"
                        filled
                        rounded
                        rows="1"
                        row-height="15"
                        append-icon="mdi-send"
                        @click:append="sendComment(post.content, post)"
                      ></v-textarea>
                    </div>
                    <div v-for="comment in post.comments"
                         :key="comment.id"
                         class="px-4">
                         <strong>{{ comment.owner.username }}</strong> - {{ comment.content }}
                    </div>
                    </div>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import axios from 'axios';
export default {
  name: "Feed",
  mounted() {
    this.loadUser()
    this.fetchPosts()
  },
  data: () => ({
    currentUser: '',
    feedPosts: {},
    userFirstname: '',
    userLastname: '',
    likeBtn: false,
  }),
  methods: {
    loadUser(){
      this.currentUser = this.$session.get('current_user')
    },
    fetchPosts() {
      this.showPostDialog = false
      axios.get('http://localhost:8000/content/post').then(response => {
         this.feedPosts = response.data
         console.log(this.feedPosts)
       }).catch(e => {
         console.log(e)
       })
    },
    sendComment(comment, post) {
      if (typeof comment !== 'undefined') {
        this.showPostDialog = false
        var token = this.$session.get('token')
        delete(post.content)
        var formData = new FormData()
        formData.append("post", post.id)
        formData.append("content", comment)
        axios.post('http://localhost:8000/content/comment/', formData, {headers: {Authorization: 'JWT ' + token}}).then(response => {
          this.feedPosts = response.data
          console.log(this.feedPosts)
          this.fetchPosts()
        }).catch(e => {
          console.log(e)
        })
      }
    }
  }
}
</script>

<style>
</style>