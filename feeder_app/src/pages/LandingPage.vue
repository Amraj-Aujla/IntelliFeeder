<template>
  <q-page class="row items-center justify-evenly q-pa-xl" style="max-height: 500px;">

    <!-- container for landing page content -->
    <div class="col-6 q-gutter-lg-md">
      <div class="text-h2 text-weight-bold" style="color: #00a6fb">CPEN 291 PROJECT 2</div>
      <div class="text-h5" style="color: #00a6fb">By Group G-16</div>

      <!-- main paragraph/product blurb -->
      <div style="margin-top: 5%;" class="text-h6"> Intelli Feeder is the perfect solution for pet owners who want to make sure
        their furry friends are well-fed and taken care of, even when they're not at home.
        Our automatic pet feeder allows you to schedule up to 4 meals per day, with adjustable
        portion sizes and feeding times. This allows you to customize your pet's feeding schedule
        and fit their unique needs and dietary requirements.</div>

      <!-- button to main page -->
      <q-btn rounded unelevated class="get-started gradient" to="/feeder" text-color="white" label="Get Started"/>
    </div>

    <!-- girl and cat svg image -->
    <div class="col-6 q-gutter-lg-md q-pa-md">
      <q-img style="margin-left: 40px;" src="~/assets/girl_n_cat.svg"/>
    </div>
  </q-page>
</template>

<script setup lang="ts">

// basic logging for page status
console.log('landing page')
</script>

<style lang="scss">

/* gradient background for the get started button */
.gradient {
  background-image:  linear-gradient(-45deg, #6f7bf7, #12cff3, #338AFF, #30c5d2);
  animation: anime 14s linear infinite; /* animate for the gradient */
  background-repeat: no-repeat;
  background-clip: padding-box;
  background-size: 600%;
}

/* formatting for the get started button */
.get-started {
  margin-top: 15%;
  color: #00a6fb;
  height: 75px;
  width: 400px;
  margin-left: 14%;
  font-size: 20px;
  border-radius: 50px;
}

/* animation for the gradient background by sliding gradient back and forth*/
@keyframes anime {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}
</style>
