<template>
<div>
    <Index></Index>
    <input id="stockId" placeholder="請輸入代號">
    <button class="btn btn-primary" name="送出" value="送出" type="submit" @click="addStock">送出</button>
    <div class="container">
      <table class="row">
          <tr class="row row-cols-3">
              <th class="col">代號</th>
              <th class="col">價格</th>
              <th class="col-2 ">選項</th>
          </tr>
          <tr v-for="item in msg" :key=item.id class="row row-cols-3">
              <td class="col">{{ item.id }} </td>
              <td class="col">{{ item.price }}</td>
              <button class="btn btn-danger col-2" type="submit" @click="removePrice(item.id)"> 刪除 </button>
          </tr>
      </table>
    </div>
</div>
</template>
<script setup>
import axios from 'axios';
import Index from './Index.vue';
</script>
<script>
/* eslint-disable */
export default {
  name: 'Price',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getStockPrice() {
      const path = 'http://localhost:5000/realPrice';
      axios.get(path)
        .then((res) => {
          console.log(res);
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          console.error(error);
        });
    },
    addStock() {
      const stockId = document.getElementById('stockId').value;
      console.log(stockId);
      const path = 'http://localhost:5000/addPrice';
      axios.post(path, {id:stockId})
        .then((res) => {
          console.log(res);
          this.msg = res.data;
        })
        .catch((error) => {
          console.log(error);
          console.error(error);
        });
    },
    removePrice(stockId) {
      console.log(stockId)
      const path = 'http://localhost:5000/removePrice';
      axios.post(path, { id: stockId } )
        .then((res) => {
          console.log(res);
          this.msg = res.data;
        })
        .catch((error) => {
          console.log(error);
          console.error(error);
        });
    },
  },
  created() {
    this.getStockPrice();
  },
};
</script>
<style>
table tr {
    margin: 15px;
}
</style>