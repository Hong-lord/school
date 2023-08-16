<template>
  <div class="banner">
    <el-carousel height="400px">
      <el-carousel-item v-for="item in banner_list" :key="item">
          <router-link :to="item.link">
          <img :src='item.img' :alt="item.name">
          </router-link>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Banner",
  data() {
    return {
      banner_list: []
    }
  },
  created() {
    // 当banner组件一创建,就向后端发请求拿回轮播图数据
    axios.get(this.$settings.base_url + '/home/banner/').then(response => {
      console.log(response.data)
      this.banner_list=response.data
    }).catch(errot => {
    })
  },

}
</script>

<style scoped>
.el-carousel__item {
  height: 400px;
  min-width: 1200px;
}

.el-carousel__item img {
  height: 400px;
  margin-left: calc(50% - 1920px / 2);
}
</style>