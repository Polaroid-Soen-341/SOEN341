<template>
    <v-container grid-list-md>
      <v-layout row wrap align-center justify-center fill-height>
        <v-flex xs12 sm8 lg4 md6>
          <v-card class="login-card mt-16">
            <v-card-title class="white--text pl-4 login" style="background-color: #512DA8">
              <span class="text-h5 headline">Polaroid</span>
            </v-card-title>

            <v-spacer/>

            <v-card-text>

              <v-layout
                row
                fill-height
                justify-center
                align-center
                v-if="loading"
              >
                <v-progress-circular
                  :size="50"
                  color="primary"
                  indeterminate
                />
              </v-layout>


              <v-form v-else ref="form" v-model="newUserValid" lazy-validation>
                <v-container>
                  <v-text-field
                    v-model="newUser.firstname"
                    :counter="70"
                    label="First Name"
                    maxlength="70"
                    required
                    outlined
                    :rules="registerRules.firstname"/>

                  <v-text-field
                    v-model="newUser.lastname"
                    :counter="70"
                    label="Last Name"
                    maxlength="70"
                    required
                    outlined
                    :rules="registerRules.lastname"/>

                  <v-text-field
                    v-model="newUser.email"
                    :counter="30"
                    label="Email"
                    maxlength="30"
                    required
                    outlined
                    :rules="registerRules.email"/>

                  <v-text-field
                    type="password"
                    v-model="newUser.password"
                    :counter="20"
                    label="Password"
                    maxlength="20"
                    required
                    outlined
                    :rules="registerRules.password"/>

                  <!-- <v-text-field
                    type="password"
                    v-model="confirmPassword"
                    :counter="20"
                    label="Confirm Password"
                    maxlength="20"
                    required
                    outlined
                    :rules="registerRules.confirmPassword"
                    /> -->
                </v-container>
                <v-divider class="mt-1 mb-3"></v-divider>
                <v-btn class="white--text" color="deep-purple darken-2" block small :disabled="!newUserValid" @click="submit()">Submit</v-btn>

              </v-form>
            </v-card-text>
          </v-card>

        </v-flex>
      </v-layout>
    </v-container>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Login',
  data: () => ({
      newUser: {},
      newUserValid: true,
      loading: false,
      confirmPassword: '',
      registerRules: {
        firstname: [
          v => !!v || 'Firstname is required',
          v => (v && v.length > 1) || 'A firstname must be more than 1 characters long',
          v => /^[a-z]+$/.test(v) || 'A firstname can only contain letters'
        ],
        lastname: [
          v => !!v || 'Lastname is required',
          v => (v && v.length > 1) || 'A lastname must be more than 1 characters long',
          v => /^[a-z]+$/.test(v) || 'A lastname can only contain letters'
        ],
        email: [
          v => !!v || 'Email is required',
          v => (v && v.length > 3) || 'A username must be more than 3 characters long',
          v => /^[a-z0-9_]+$/.test(v) || 'A username can only contain letters and digits'
        ],
        password: [
          v => !!v || 'Password is required',
          v => (v && v.length > 7) || 'The password must be longer than 7 characters'
        ]
        // confirmPassword: [
        //   v => !!v || 'Confirm Password is required',
        //   v => (v === this.newUser.password) || 'Confirm password must match your password'
        // ]
      }
  }),
  methods: {
      submit() {
        if (this.$refs.form.validate()) {
            this.loading = true;
            axios.post('http://localhost:8000/auth/create/', this.newUser).then(response => {
              console.log(response)
              this.$router.push('/');
            }).catch(e => {
              // this.snackbar = true
              this.loading = false
              console.log(e)
            })
          }
      }
  },
  computed: {
    // passwordConfirmationRule() {
    //     return () => (this.newUser.password === this.newUser.confirmPassword) || 'Passwords must match'
    // },
  }
}
</script>
<style>
.login {
  background-color: rgb(225 48 108);
}
</style>
