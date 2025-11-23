<template>
  <div class="container">
    <h1>🫀 SimCardiac 数字孪生心脏 </h1>
    <p class="subtitle">实验 {{ experimentId }} (尚未完工) </p>
    <div v-if="error" class="error">{{ error }}</div>
    <div v-if="loading" class="loading">加载数据中...</div>
    <div v-else>
      <div class="controls">
        <button @click="togglePlay">
          {{ isPlaying ? '⏸ 暂停' : '▶ 播放' }}
        </button>
        <div class="time-display">时间: {{ currentImageTime }} s</div>
        <div class="value-display">LAD4: {{ currentLAD4Value }} mmHg</div>
      </div>
      <div class="content-grid">
        <div class="image-container">
          <img :src="currentImageUrl" :alt="'图片 ' + currentImageIndex" />
        </div>
        <div class="chart-container">
          <canvas ref="chartCanvas"></canvas>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, nextTick } from 'vue'
import { Chart, registerables } from 'chart.js'

Chart.register(...registerables)

// 配置参数
const DATA_FILE = import.meta.env.BASE_URL + 'coronary_Q_43.json'  // 数据文件路径
const TIME_STEP = 0.0001                   // 时间步长（秒）
const MAX_POINTS = 800                   // 最大显示数据点数
const HIGHLIGHT_STEP = 1                 // 每次高亮点移动的步长
const ANIMATION_INTERVAL = 20           // 动画间隔（毫秒）
const TIME_DECIMALS = 2                  // 时间标签小数位数
const VALUE_DECIMALS = 6                 // 数值显示小数位数
const IMAGE_INTERVAL = 0.2               // 图片切换间隔（秒）
const TOTAL_IMAGES = 10                  // 总图片数量

const loading = ref(true)
const error = ref(null)
const experimentId = ref(null)
const chartCanvas = ref(null)
const isPlaying = ref(true)
const currentImageIndex = ref(1)
const highlightIndexRef = ref(0)
let chart = null
let highlightIndex = 0
let animationTimer = null
let data = []
let step = 1  // 采样步长

const currentImageUrl = computed(() => 
  import.meta.env.BASE_URL + `figures/${currentImageIndex.value}.jpg`
)

const currentImageTime = computed(() => {
  // 使用折线图的实际时间：highlightIndex * step * TIME_STEP
  return (highlightIndexRef.value * step * TIME_STEP).toFixed(TIME_DECIMALS)
})

const currentLAD4Value = computed(() => {
  if (data.length === 0) return '0.000000'
  return data[highlightIndexRef.value]?.toFixed(VALUE_DECIMALS) || '0.000000'
})

const loadData = async () => {
  try {
    const res = await fetch(DATA_FILE)
    if (!res.ok) throw new Error('无法加载数据文件')
    
    const json = await res.json()
    experimentId.value = json.experiment
    
    const key = Object.keys(json.data)[0]
    const rawData = json.data[key].value
    
    // 按间隔采样，最多取MAX_POINTS个数据点
    step = Math.ceil(rawData.length / MAX_POINTS)
    data = rawData.filter((_, i) => i % step === 0).slice(0, MAX_POINTS)
    
    loading.value = false
    await nextTick()
    
    if (chart) chart.destroy()
    
    chart = new Chart(chartCanvas.value, {
      type: 'line',
      data: {
        labels: data.map((_, i) => (i * step * TIME_STEP).toFixed(TIME_DECIMALS)),
        datasets: [{
          label: key,
          data,
          /* 主色调：深蓝 */
          borderColor: '#2b6cb0',
          backgroundColor: 'rgba(43,108,176,0.08)',
          borderWidth: 1,
          pointRadius: (ctx) => ctx.dataIndex === highlightIndex ? 4 : 0,
          pointBackgroundColor: (ctx) => ctx.dataIndex === highlightIndex ? '#ff6b6b' : '#2b6cb0',
          tension: 0.12
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        interaction: { mode: 'index', intersect: false },
        plugins: {
          title: { display: true, text: '冠状动脉流量随时间变化' },
          tooltip: {
            callbacks: {
              title: ctx => '时间: ' + ctx[0].label + ' s',
              label: ctx => ctx.dataset.label + ': ' + ctx.parsed.y.toFixed(VALUE_DECIMALS)
            }
          }
        },
        scales: {
          x: { title: { display: true, text: '时间 (秒)' } },
          y: { title: { display: true, text: '流量值' } }
        }
      }
    })
    
    startAnimation()
  } catch (err) {
    error.value = '加载数据失败: ' + err.message
    loading.value = false
  }
}

const startAnimation = () => {
  if (animationTimer) return
  animationTimer = setInterval(() => {
    highlightIndex = (highlightIndex + HIGHLIGHT_STEP) % data.length
    highlightIndexRef.value = highlightIndex
    
    // 根据实际时间计算图片索引
    const currentTime = highlightIndex * step * TIME_STEP
    const imageIndex = Math.floor(currentTime / IMAGE_INTERVAL) % TOTAL_IMAGES + 1
    currentImageIndex.value = imageIndex
    
    chart.update('none')
  }, ANIMATION_INTERVAL)
}

const stopAnimation = () => {
  if (animationTimer) {
    clearInterval(animationTimer)
    animationTimer = null
  }
}

const togglePlay = () => {
  isPlaying.value = !isPlaying.value
  isPlaying.value ? startAnimation() : stopAnimation()
}

onMounted(loadData)
onUnmounted(() => stopAnimation())
</script>
