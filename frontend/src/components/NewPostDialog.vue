<template>
  <div class="text-center">
    <v-dialog
      v-model="showDialog"
      persistent
      width="800">
      <v-card>
        <v-card-title class="headline white--text blue">
          New Post
        </v-card-title>

        <v-file-input v-model="image"
                      :rules="rules"
                      class="px-8"
                      accept="image/png, image/jpeg, image/bmp"
                      prepend-icon="mdi-camera"
                      label="Picture"/>
        <v-textarea v-model="comment"
                    class="px-8"
                    prepend-inner-icon="mdi-comment"
                    counter
                    outlined
                    name="input-7-4"
                    label="Comment on post"
        ></v-textarea>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            class="white--text text-capitalize"
            color="blue"
            @click="saveClicked()">
            Post
          </v-btn>
          <v-btn
            class="white--text text-capitalize"
            outlined
            color="blue"
            @click="cancelClicked()">
            Cancel
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
  export default {
    name: 'PostDialog',
    props: ['showDialog'],
    data () {
      return {
        image: null,
        comment: '',
        rules: [
        value => !value || value.size < 2000000 || 'Avatar size should be less than 2 MB!',
      ]
      }
    },
    methods: {
      saveClicked() {
        this.comment = ''
        this.image = null
        this.$emit('cancelClicked')
      },
      cancelClicked() {
        this.comment = ''
        this.image = null
        this.$emit('cancelClicked')
      }
    }
  }
</script>