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
                    v-model="newUser.first_name"
                    :counter="20"
                    label="First Name"
                    maxlength="20"
                    required
                    outlined
                    :rules="registerRules.firstname"/>

                  <v-text-field
                    v-model="newUser.last_name"
                    :counter="20"
                    label="Last Name"
                    maxlength="20"
                    required
                    outlined
                    :rules="registerRules.lastname"/>

                  <v-text-field
                    v-model="newUser.username"
                    :counter="20"
                    label="Username"
                    maxlength="20"
                    required
                    outlined
                    :rules="registerRules.username"/>

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
                    :counter="30"
                    label="Password"
                    maxlength="30"
                    required
                    outlined
                    :rules="registerRules.password"/>

                  <v-text-field
                    type="password"
                    v-model="confirmPassword"
                    :counter="30"
                    label="Confirm Password"
                    maxlength="30"
                    required
                    outlined
                    :rules="[registerRules.confirmPassword, passwordConfirmationRule]"/>
                </v-container>
                <v-divider class="mt-1 mb-3"></v-divider>
                <v-btn class="white--text" color="deep-purple darken-2" block small :disabled="!newUserValid" @click="submit()">Submit</v-btn>

              </v-form>
            </v-card-text>
          </v-card>

          <v-snackbar v-model="snackbarError"
                      :timeout="timeout"
                      absolute
                      bottom
                      color="red darken-2">
                      {{ errorMessage }}
          </v-snackbar>

          <v-snackbar v-model="snackbarApproved"
                      :timeout="timeout"
                      absolute
                      bottom
                      color="success">
                      {{ approvedMessage }}
          </v-snackbar>

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
      confirmPassword: null,
      snackbarError: false,
      errorMessage: 'Unable to create new account!',
      snackbarApproved: false,
      approvedMessage: 'New Account successfully created!',
      timeout: 5000,
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
        username: [
          v => !!v || 'Username is required',
          v => (v && v.length > 1) || 'A username must be more than 1 characters long',
          v => /^[a-z0-9_]+$/.test(v) || 'A username can only contain letters'
        ],
        email: [
          v => !!v || 'Email is required',
          v => !v || /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid'
        ],
        password: [
          v => !!v || 'Password is required',
          v => (v && v.length > 7) || 'Password must be at least 8 characters long'
        ],
        confirmPassword: [
          v => !!v || 'Confirm Password is required'
        ],
      }
  }),
  methods: {
      submit() {
        if (this.$refs.form.validate()) {
            this.loading = true;
            axios.post('http://localhost:8000/api-auth/user/create/', this.newUser).then(response => {
              this.snackbarApproved = true
              console.log(response)
              this.$router.push('/');
            }).catch(e => {
              this.snackbarError = true
              this.loading = false
              console.log(e)
            })
          }
      }
  },
  computed: {
    passwordConfirmationRule() {
      return (this.newUser.password === this.confirmPassword) || 'Passwords must match'
    }
  }
}
</script>
<style>
.login {
  background-color: rgb(225 48 108);
}
</style>
