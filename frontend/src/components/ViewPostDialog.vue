<template>
  <div class="text-center">
    <v-dialog
      v-model="showDialog"
      persistent
      width="800">
      <v-card>
        <v-card-title class="headline white--text blue mb-4">
         Post Details
         <v-btn style="position: absolute; right: 6px; top: 16px"
                small
                icon
                color="white"
                @click="cancelClicked()">
                <v-icon>mdi-window-close</v-icon>
          </v-btn>
        </v-card-title>

        <v-card-text>
          <div>
            <v-img
              :src="postDetails.picture"
              :lazy-src="postDetails.picture"
              aspect-ratio="1"
              class="grey lighten-2 mx-4 mb-4">
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
            <div class="px-4 pb-2">
              <strong>{{ postDetails.owner.username }}</strong> - {{ postDetails.description }}
            </div>
            <div class="px-4">
              <v-textarea
                label="Add comment..."
                auto-grow
                v-model="postDetails.content"
                filled
                rounded
                rows="1"
                row-height="15"
                append-icon="mdi-send"
                @click:append="sendComment(postDetails.content, postDetails)"
              ></v-textarea>
            </div>
            <div v-for="comment in postDetails.comments"
                  :key="comment.id"
                  class="px-4">
                  <strong>{{ comment.owner.username }}</strong> - {{ comment.content }}
            </div>
          </div>
        </v-card-text>

      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'ViewPostDialog',
  props: ['showDialog', 'postDetails'],
  data () {
    return {
      loading: false,
      // rules: {comment: [v => !!v || 'Comment must not be empty']}
    }
  },
  methods: {
    sendComment(comment, post) {
      if (typeof comment !== 'undefined') {
        var token = this.$session.get('token')
        delete(post.content)
        var formData = new FormData()
        formData.append("post", post.id)
        formData.append("content", comment)
        axios.post('http://localhost:8000/content/comment/', formData, {headers: {Authorization: 'JWT ' + token}}).then(response => {
          this.feedPosts = response.data
          console.log(this.feedPosts)
        }).catch(e => {
          console.log(e)
        })
      }
    },
    cancelClicked() {
      this.$emit('cancelClicked')
    }
  }
}
</script>