<script>
	import {Howl} from 'howler'

  let features = [
    {
      icon: '<svg width="80px" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" d="m21.9 42-6.4-6.4 2.15-2.1 4.25 4.25 8.45-8.5 2.15 2.15ZM9 12h30V9H9v3Zm6.95 6h16.1l.9-3h-17.9l.9 3Zm0 3q-.95 0-1.75-.575T13.1 18.9L11.85 15H9q-1.25 0-2.125-.875T6 12V6h36v6q0 1.25-.875 2.125T39 15h-2.85l-1.5 4.05q-.35.85-1.125 1.4-.775.55-1.725.55ZM9 12V9v3Z"/></svg>',
      text: '98% Accuration'
    },
    {
      icon: '<svg width="80px" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" d="M20.45 31.75q1.15 1.15 3.325 1.075 2.175-.075 3.175-1.625l8.95-14q.35-.55-.075-.975-.425-.425-.975-.075L21 25.2q-1.5 1-1.6 3.2-.1 2.2 1.05 3.35ZM9.7 40q-.85 0-1.675-.425Q7.2 39.15 6.8 38.35q-1.3-2.4-2-4.875T4.1 28.2q0-4.15 1.575-7.825t4.275-6.4q2.7-2.725 6.325-4.325T24 8.05q2.25 0 4.7.575t4.85 1.925q1 .55 1.1 1.325.1.775-.5 1.275-.4.3-.925.375-.525.075-.975-.175-2.1-1.15-4.35-1.725-2.25-.575-3.9-.575-7 0-11.95 5-4.95 5-4.95 12.15 0 2.25.625 4.55T9.5 37h28.95q1.1-1.8 1.75-4.2.65-2.4.65-4.7 0-1.85-.475-3.95t-1.625-4q-.3-.5-.2-1.025.1-.525.5-.875.55-.45 1.2-.325.65.125 1 .725 1.25 2.3 1.9 4.575.65 2.275.7 4.575.05 3-.625 5.65-.675 2.65-2.025 4.9-.6 1.15-1.275 1.4-.675.25-1.675.25ZM24 24Z"/></svg>',
      text: 'Fast'
    },
    {
      icon: '<svg width="80px" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" d="M29.9 31.4q-.3 0-.55-.1-.25-.1-.5-.35l-6.4-6.4q-.45-.45-.425-1.05.025-.6.475-1.05.45-.45 1.05-.45.6 0 1.05.45l5.3 5.3 10.9-10.9q.45-.45 1.05-.45.6 0 1.05.45.45.45.45 1.075T42.9 19L30.95 30.95q-.25.25-.5.35-.25.1-.55.1ZM33 41.5H11V43h22Zm0-35V5H11v1.5ZM11 46q-1.25 0-2.125-.875T8 43V5q0-1.25.875-2.125T11 2h22q1.25 0 2.125.875T36 5v7.3h-3V9.5H11v29h22v-2.8h3V43q0 1.25-.875 2.125T33 46Zm0-41v1.5V5Zm0 38v-1.5V43Z"/></svg>',
      text: 'Easy To Use'
    },
    {
      icon: '<svg width="80px" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" d="m32.05 43.95-5-5q-.45-.45-.45-1.05 0-.6.45-1.05.45-.45 1.05-.45.6 0 1.05.45l3.9 3.9 8.15-8.15q.45-.45 1.05-.425.6.025 1.05.475.4.45.4 1.075t-.4 1.025l-9.15 9.2q-.4.45-1.025.45-.625 0-1.075-.45ZM18 30.1l-2.5 2.5q-.45.45-1.05.45-.6 0-1.05-.45-.45-.45-.45-1.05 0-.6.45-1.05l2.5-2.5-2.5-2.5q-.45-.45-.45-1.05 0-.6.45-1.05.45-.45 1.05-.45.6 0 1.05.45l2.5 2.5 2.5-2.5q.45-.45 1.05-.45.6 0 1.05.45.45.45.45 1.05 0 .6-.45 1.05L20.1 28l2.5 2.5q.45.45.45 1.05 0 .6-.45 1.05-.45.45-1.05.45-.6 0-1.05-.45ZM9 44q-1.2 0-2.1-.9Q6 42.2 6 41V10q0-1.2.9-2.1Q7.8 7 9 7h3.25V5.6q0-.7.45-1.15.45-.45 1.15-.45t1.175.45q.475.45.475 1.15V7h17V5.6q0-.7.45-1.15Q33.4 4 34.1 4t1.175.45q.475.45.475 1.15V7H39q1.2 0 2.1.9.9.9.9 2.1v17.6l-3 3V19.5H9V41h15.85l3 3Zm0-27.5h30V10H9Zm0 0V10v6.5Z"/></svg>',
      text: 'Free'
    }
  ]
  
	let sound = new Howl({
		src: ['http://127.0.0.1:5173/features.wav']
	});
</script>

<div class="flex justify-center items-center flex-col gap-24 bg-gradient-to-bl from-black via-black to-emerald-950 relative mt-32">
  <h2 class="text-3xl md:text-5xl tracking-loose text-center drop-shadow-[0_8px_6px_rgba(34,197,94,1)] bg-clip-text text-transparent bg-gradient-to-r from-teal-400 to-emerald-400 font-bold">Why Using This Tools?</h2>
  <div class="flex flex-col justify-center items-center gap-16 text-center">
    {#each features as f}
      <div class="group relative hover:left-[-40%]" on:click={() => sound.play()}>
        <div class="flex flex-col gap-4 justify-center items-center bg-gradient-to-b from-teal-500 via-emerald-950 to-black p-8 w-[160px] rounded-tr-3xl rounded-bl-3xl text-green-100 z-[1] relative shadow-lg shadow-emerald-500">
        {@html f.icon}
         <p class="text-xl font-bold">{ f.text }</p>
        </div>
        <div class="bg-black text-white rounded-tl-3xl rounded-br-3xl absolute top-[24px] left-[80%] bottom-[-24px] w-[160px] bg-gradient-to-tr from-teal-500 via-emerald-800 to-green-900 flex items-center justify-center hidden group-hover:flex shadow-lg shadow-emerald-500">
          <p class="text-justify pl-6 text-sm text-green-100">Penjelasan</p>
        </div>
      </div>
    {/each}
  </div>
</div>