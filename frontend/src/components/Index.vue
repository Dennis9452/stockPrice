<script setup>
import { ref, reactive,onMounted } from 'vue'
  // const emit = defineEmits(['LEFTMenu-click','LEFTMenu-onFocus'])
  let leftBanner = [
    { id:'search', title: '搜尋', index: 0 }, 
    { id:'home', title: '首頁', index: 1 }, 
    { id:'filter', title: '篩選', index: 2 }, 
    { id:'vod', title: '媒體庫', index: 3 }, 
    { id:'setting', title: '設定', index: 4 }
  ] 
</script>

<template>
  <div class="row">
    <div v-for="item in leftBanner" :key="item.id" :class="item.id" class="col" >
      <router-link :to="{path : item.id}">{{ item.title }}</router-link>
    </div>
    <router-view></router-view>
  </div>
</template>