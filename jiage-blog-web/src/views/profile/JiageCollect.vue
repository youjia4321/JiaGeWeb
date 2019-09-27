<template>
  <JiageContent :title="title">
    <Card slot="main-content"></Card>
  </JiageContent>
</template>

<script>
import JiageContent from "@/components/JiageContent";

export default {
  data() {
    return {
      title: "我的收藏"
    };
  },
  components: {
    JiageContent
  }
};
</script>

<style>
</style>