---
id: Compass
section: components
wrapperTag: div
---## Examples

### Card view

This demo populates the main Compass section with a card view, which is one of the more common page types used within a Compass layout. In this demo, the page includes:

* A `.pf-v6-c-compass__main-header` that contains the page title and toolbar with action items.
* A `.pf-v6-c-compass__content`, which contains a glass panel component to create a rounded-rectangle container that serves as the main content background.

```html isFullscreen isBeta
<div class="pf-v6-c-compass pf-m-animate-smoothly">
  <div class="pf-v6-c-compass__container">
    <div class="pf-v6-c-compass__header pf-m-expanded">
      <div class="pf-v6-c-compass__logo">
        <svg
          width="192"
          height="39"
          viewBox="0 0 192 39"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          aria-hidden="true"
        >
          <path
            d="M33.3807 22.9001C36.6672 22.9001 41.4287 22.2167 41.4287 18.2926C41.4287 17.9865 41.4209 17.6883 41.3472 17.3901L39.3885 8.85069C38.9336 6.97444 38.5392 6.11944 35.2501 4.47014C32.7023 3.16125 27.1468 1 25.5035 1C23.9733 1 23.5211 2.98972 21.7069 2.98972C19.8927 2.98972 18.6465 1.51194 17.0032 1.51194C15.3599 1.51194 14.395 2.59389 13.6036 4.81056C13.6036 4.81056 11.3924 11.0674 11.1085 11.9778C11.0506 12.1493 11.0506 12.3393 11.0506 12.4897C11.0506 14.9228 20.5921 22.9001 33.3833 22.9001M41.9414 19.8839C42.3963 22.0451 42.3963 22.2721 42.3963 22.5571C42.3963 26.2542 38.2579 28.3019 32.818 28.3019C20.5185 28.3019 9.74918 21.0767 9.74918 16.3003C9.74918 15.5614 9.92008 14.8779 10.1462 14.366C5.72383 14.5929 0 15.3899 0 20.4539C0 28.7585 19.6114 39 35.1396 39C47.0421 39 50.0447 33.5956 50.0447 29.3285C50.0447 25.9718 47.1552 22.1612 41.9388 19.8839"
            fill="#EE0000"
          />
          <path
            d="M41.9386 19.8864C42.3935 22.0477 42.3935 22.2746 42.3935 22.5596C42.3935 26.2567 38.255 28.3045 32.8152 28.3045C20.5157 28.3045 9.74634 21.0792 9.74634 16.3028C9.74634 15.5639 9.91724 14.8804 10.1434 14.3685L11.1083 11.9777C11.0504 12.1492 11.0504 12.3392 11.0504 12.4896C11.0504 14.9227 20.5919 22.9 33.3831 22.9C36.6696 22.9 41.4312 22.2165 41.4312 18.2925C41.4312 17.9864 41.4233 17.6882 41.3496 17.39L41.9412 19.8864H41.9386Z"
            fill="black"
          />
          <path
            d="M75.764 16V1.29995H82.295C83.261 1.29995 84.115 1.48895 84.857 1.86695C85.599 2.24495 86.173 2.76995 86.579 3.44195C86.999 4.09995 87.209 4.86995 87.209 5.75195C87.209 6.70395 86.943 7.53695 86.411 8.25095C85.893 8.95095 85.186 9.46195 84.29 9.78395L87.398 16H84.605L81.77 10.12H78.284V16H75.764ZM78.284 8.10395H82.064C82.848 8.10395 83.478 7.89395 83.954 7.47395C84.43 7.03995 84.668 6.47295 84.668 5.77295C84.668 5.05895 84.43 4.49195 83.954 4.07195C83.478 3.63795 82.848 3.42095 82.064 3.42095H78.284V8.10395Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M93.9392 16.21C92.9312 16.21 92.0212 15.972 91.2092 15.496C90.3972 15.006 89.7532 14.3549 89.2772 13.5429C88.8012 12.7169 88.5632 11.7859 88.5632 10.75C88.5632 9.71395 88.7872 8.78995 89.2352 7.97795C89.6832 7.16595 90.2922 6.52195 91.0622 6.04595C91.8462 5.55595 92.7142 5.31095 93.6662 5.31095C94.6462 5.31095 95.5072 5.54895 96.2492 6.02495C97.0052 6.50095 97.5932 7.14495 98.0132 7.95695C98.4472 8.76895 98.6642 9.69995 98.6642 10.75V11.3169H90.8942C90.9782 11.8909 91.1602 12.4019 91.4402 12.8499C91.7342 13.2839 92.1052 13.627 92.5532 13.879C93.0152 14.1309 93.5122 14.257 94.0442 14.257C94.5342 14.257 94.9962 14.173 95.4302 14.005C95.8782 13.823 96.2492 13.578 96.5432 13.2699L98.0972 14.677C97.4532 15.209 96.7952 15.601 96.1232 15.853C95.4652 16.091 94.7372 16.21 93.9392 16.21ZM90.9152 9.84695H96.4172C96.3332 9.34295 96.1582 8.89495 95.8922 8.50295C95.6402 8.11095 95.3182 7.80295 94.9262 7.57895C94.5482 7.35495 94.1282 7.24295 93.6662 7.24295C93.2042 7.24295 92.7772 7.35495 92.3852 7.57895C92.0072 7.78895 91.6922 8.08995 91.4402 8.48195C91.1882 8.87395 91.0132 9.32895 90.9152 9.84695Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M105.388 16.1049C104.506 16.1049 103.708 15.867 102.994 15.391C102.28 14.901 101.706 14.257 101.272 13.459C100.852 12.6469 100.642 11.7439 100.642 10.75C100.642 9.74195 100.859 8.83895 101.293 8.04095C101.727 7.22895 102.315 6.58495 103.057 6.10895C103.813 5.63295 104.646 5.39495 105.556 5.39495C106.158 5.39495 106.718 5.51395 107.236 5.75195C107.768 5.97595 108.23 6.31195 108.622 6.75995V0.94295L110.995 0.522949V16H108.643V14.6139C108.265 15.0899 107.796 15.461 107.236 15.727C106.676 15.979 106.06 16.1049 105.388 16.1049ZM106.123 14.11C106.627 14.11 107.096 14.012 107.53 13.816C107.964 13.606 108.328 13.319 108.622 12.955V8.52395C108.314 8.15995 107.943 7.87995 107.509 7.68395C107.075 7.48795 106.613 7.38995 106.123 7.38995C105.521 7.38995 104.982 7.53695 104.506 7.83095C104.044 8.11095 103.673 8.50295 103.393 9.00695C103.113 9.51095 102.973 10.092 102.973 10.75C102.973 11.38 103.113 11.9539 103.393 12.4719C103.673 12.976 104.044 13.375 104.506 13.669C104.982 13.9629 105.521 14.11 106.123 14.11Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M118.848 16V1.29995H121.368V7.47395H128.676V1.29995H131.196V16H128.676V9.72095H121.368V16H118.848Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M137.314 16.189C136.586 16.189 135.935 16.056 135.361 15.79C134.801 15.51 134.36 15.132 134.038 14.656C133.73 14.166 133.576 13.606 133.576 12.976C133.576 12.346 133.737 11.7999 134.059 11.3379C134.395 10.8759 134.864 10.519 135.466 10.267C136.068 10.015 136.782 9.88895 137.608 9.88895C138.098 9.88895 138.581 9.94495 139.057 10.0569C139.533 10.1549 139.995 10.323 140.443 10.561V9.38495C140.443 8.68495 140.24 8.15995 139.834 7.80995C139.442 7.45995 138.84 7.28495 138.028 7.28495C137.594 7.28495 137.125 7.35495 136.621 7.49495C136.131 7.62095 135.578 7.82395 134.962 8.10395L134.122 6.38195C135.662 5.66795 137.118 5.31095 138.49 5.31095C139.862 5.31095 140.919 5.64695 141.661 6.31895C142.417 6.97695 142.795 7.91495 142.795 9.13295V16H140.443V14.908C139.995 15.342 139.512 15.6639 138.994 15.874C138.476 16.084 137.916 16.189 137.314 16.189ZM135.802 12.934C135.802 13.424 135.998 13.809 136.39 14.089C136.782 14.3689 137.307 14.509 137.965 14.509C138.441 14.509 138.882 14.439 139.288 14.299C139.708 14.1449 140.093 13.9209 140.443 13.627V11.926C140.079 11.7579 139.701 11.6319 139.309 11.5479C138.917 11.464 138.49 11.422 138.028 11.422C137.342 11.422 136.796 11.5549 136.39 11.8209C135.998 12.0869 135.802 12.458 135.802 12.934Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M149.897 16.21C148.833 16.21 148.028 15.9649 147.482 15.4749C146.936 14.971 146.663 14.236 146.663 13.2699V7.36895H144.563V5.47895H146.663V2.58095L149.036 2.07695V5.47895H151.955V7.36895H149.036V12.745C149.036 13.2629 149.148 13.634 149.372 13.858C149.596 14.068 149.974 14.1729 150.506 14.1729C150.744 14.1729 150.961 14.1589 151.157 14.1309C151.367 14.089 151.626 14.0189 151.934 13.9209V15.9159C151.64 16.0139 151.304 16.084 150.926 16.1259C150.562 16.1819 150.219 16.21 149.897 16.21Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M73.916 38L79.964 23.2999H83.471L89.456 38H86.159L84.668 34.1359H78.599L77.087 38H73.916ZM79.544 31.6999H83.744L81.644 26.2819L79.544 31.6999Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M94.4493 38.2099C93.6093 38.2099 92.8603 38.028 92.2023 37.664C91.5583 37.286 91.0473 36.768 90.6693 36.11C90.3053 35.452 90.1233 34.6959 90.1233 33.8419V27.059H93.0003V33.422C93.0003 34.122 93.2033 34.682 93.6093 35.102C94.0293 35.522 94.5823 35.7319 95.2683 35.7319C96.2483 35.7319 97.0043 35.368 97.5363 34.6399V27.059H100.413V38H97.5363V37.118C96.6963 37.846 95.6673 38.2099 94.4493 38.2099Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M107.842 38.1679C106.625 38.1679 105.7 37.895 105.07 37.3489C104.454 36.7889 104.146 35.9769 104.146 34.9129V29.4529H101.899V27.059H104.146V24.2659L107.024 23.6149V27.059H110.153V29.4529H107.024V34.325C107.024 34.829 107.136 35.193 107.36 35.417C107.583 35.6269 107.975 35.7319 108.535 35.7319C108.815 35.7319 109.068 35.7179 109.292 35.6899C109.529 35.6479 109.789 35.5779 110.069 35.4799V37.853C109.775 37.951 109.404 38.028 108.956 38.084C108.522 38.1399 108.15 38.1679 107.842 38.1679Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M116.767 38.2099C115.675 38.2099 114.688 37.958 113.806 37.4539C112.924 36.9499 112.224 36.271 111.706 35.417C111.188 34.563 110.929 33.604 110.929 32.54C110.929 31.476 111.188 30.517 111.706 29.663C112.224 28.795 112.924 28.1089 113.806 27.6049C114.688 27.101 115.675 26.8489 116.767 26.8489C117.859 26.8489 118.846 27.101 119.728 27.6049C120.61 28.1089 121.31 28.795 121.828 29.663C122.346 30.517 122.605 31.476 122.605 32.54C122.605 33.604 122.346 34.563 121.828 35.417C121.31 36.271 120.61 36.9499 119.728 37.4539C118.846 37.958 117.859 38.2099 116.767 38.2099ZM116.767 35.7109C117.341 35.7109 117.852 35.5709 118.3 35.291C118.762 35.011 119.126 34.6329 119.392 34.1569C119.672 33.6669 119.812 33.128 119.812 32.54C119.812 31.938 119.672 31.399 119.392 30.923C119.126 30.447 118.762 30.069 118.3 29.7889C117.852 29.4949 117.341 29.3479 116.767 29.3479C116.207 29.3479 115.696 29.4949 115.234 29.7889C114.772 30.069 114.408 30.447 114.142 30.923C113.876 31.399 113.743 31.938 113.743 32.54C113.743 33.128 113.876 33.6669 114.142 34.1569C114.408 34.6329 114.772 35.011 115.234 35.291C115.696 35.5709 116.207 35.7109 116.767 35.7109Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M124.373 38V27.059H127.25V27.8989C128.034 27.1989 128.986 26.8489 130.106 26.8489C130.82 26.8489 131.457 26.996 132.017 27.2899C132.577 27.57 133.039 27.969 133.403 28.4869C134.313 27.3949 135.517 26.8489 137.015 26.8489C137.841 26.8489 138.562 27.038 139.178 27.416C139.808 27.78 140.298 28.291 140.648 28.9489C141.012 29.5929 141.194 30.3489 141.194 31.2169V38H138.338V31.6369C138.338 30.9229 138.149 30.3629 137.771 29.9569C137.393 29.5369 136.889 29.327 136.259 29.327C135.377 29.327 134.677 29.6909 134.159 30.4189C134.173 30.5449 134.187 30.6709 134.201 30.7969C134.215 30.9229 134.222 31.063 134.222 31.2169V38H131.345V31.6369C131.345 30.9229 131.156 30.3629 130.778 29.9569C130.414 29.5369 129.917 29.327 129.287 29.327C128.405 29.327 127.726 29.6629 127.25 30.3349V38H124.373Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M146.87 38.1889C146.086 38.1889 145.393 38.049 144.791 37.769C144.189 37.475 143.72 37.076 143.384 36.5719C143.048 36.0679 142.88 35.4869 142.88 34.8289C142.88 33.7789 143.272 32.9669 144.056 32.393C144.854 31.805 145.946 31.511 147.332 31.511C148.284 31.511 149.18 31.6579 150.02 31.952V31.1539C150.02 29.8799 149.25 29.243 147.71 29.243C147.248 29.243 146.751 29.32 146.219 29.4739C145.687 29.6139 145.071 29.8379 144.371 30.146L143.321 28.025C144.189 27.6329 145.015 27.3389 145.799 27.143C146.597 26.947 147.395 26.8489 148.193 26.8489C149.663 26.8489 150.804 27.2059 151.616 27.92C152.442 28.62 152.855 29.6139 152.855 30.9019V38H150.02V37.2229C149.572 37.5589 149.089 37.804 148.571 37.958C148.053 38.1119 147.486 38.1889 146.87 38.1889ZM145.61 34.7659C145.61 35.186 145.792 35.5219 146.156 35.7739C146.52 36.0119 147.003 36.131 147.605 36.131C148.571 36.131 149.376 35.893 150.02 35.417V33.8209C149.32 33.541 148.55 33.401 147.71 33.401C147.052 33.401 146.534 33.527 146.156 33.7789C145.792 34.0169 145.61 34.346 145.61 34.7659Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M159.912 38.1679C158.694 38.1679 157.77 37.895 157.14 37.3489C156.524 36.7889 156.216 35.9769 156.216 34.9129V29.4529H153.969V27.059H156.216V24.2659L159.093 23.6149V27.059H162.222V29.4529H159.093V34.325C159.093 34.829 159.205 35.193 159.429 35.417C159.653 35.6269 160.045 35.7319 160.605 35.7319C160.885 35.7319 161.137 35.7179 161.361 35.6899C161.599 35.6479 161.858 35.5779 162.138 35.4799V37.853C161.844 37.951 161.473 38.028 161.025 38.084C160.591 38.1399 160.22 38.1679 159.912 38.1679Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M163.625 38V27.059H166.502V38H163.625ZM165.053 25.757C164.605 25.757 164.22 25.596 163.898 25.274C163.576 24.952 163.415 24.5669 163.415 24.1189C163.415 23.6569 163.576 23.2719 163.898 22.9639C164.22 22.6419 164.605 22.4809 165.053 22.4809C165.515 22.4809 165.9 22.6419 166.208 22.9639C166.53 23.2719 166.691 23.6569 166.691 24.1189C166.691 24.5669 166.53 24.952 166.208 25.274C165.9 25.596 165.515 25.757 165.053 25.757Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M174.086 38.2099C172.994 38.2099 172.007 37.958 171.125 37.4539C170.243 36.9499 169.543 36.271 169.025 35.417C168.507 34.563 168.248 33.604 168.248 32.54C168.248 31.476 168.507 30.517 169.025 29.663C169.543 28.795 170.243 28.1089 171.125 27.6049C172.007 27.101 172.994 26.8489 174.086 26.8489C175.178 26.8489 176.165 27.101 177.047 27.6049C177.929 28.1089 178.629 28.795 179.147 29.663C179.665 30.517 179.924 31.476 179.924 32.54C179.924 33.604 179.665 34.563 179.147 35.417C178.629 36.271 177.929 36.9499 177.047 37.4539C176.165 37.958 175.178 38.2099 174.086 38.2099ZM174.086 35.7109C174.66 35.7109 175.171 35.5709 175.619 35.291C176.081 35.011 176.445 34.6329 176.711 34.1569C176.991 33.6669 177.131 33.128 177.131 32.54C177.131 31.938 176.991 31.399 176.711 30.923C176.445 30.447 176.081 30.069 175.619 29.7889C175.171 29.4949 174.66 29.3479 174.086 29.3479C173.526 29.3479 173.015 29.4949 172.553 29.7889C172.091 30.069 171.727 30.447 171.461 30.923C171.195 31.399 171.062 31.938 171.062 32.54C171.062 33.128 171.195 33.6669 171.461 34.1569C171.727 34.6329 172.091 35.011 172.553 35.291C173.015 35.5709 173.526 35.7109 174.086 35.7109Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M181.693 38V27.059H184.57V27.962C185.396 27.2199 186.418 26.8489 187.636 26.8489C188.49 26.8489 189.239 27.038 189.883 27.416C190.541 27.78 191.052 28.291 191.416 28.9489C191.78 29.5929 191.962 30.3489 191.962 31.2169V38H189.085V31.6369C189.085 30.9229 188.882 30.3629 188.476 29.9569C188.07 29.5369 187.517 29.327 186.817 29.327C186.327 29.327 185.893 29.425 185.515 29.621C185.137 29.803 184.822 30.0689 184.57 30.4189V38H181.693Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <line
            x1="66.5"
            y1="1.5"
            x2="66.5"
            y2="38.5"
            stroke="var(--pf-t--global--text--color--regular)"
            stroke-linecap="round"
          />
        </svg>
      </div>
      <div class="pf-v6-c-compass__nav">
        <div class="pf-v6-c-panel pf-m-pill pf-m-glass">
          <div class="pf-v6-c-panel__main">
            <div class="pf-v6-c-panel__main-body">
              <div class="pf-v6-c-compass__nav-content">
                <div class="pf-v6-c-compass__nav-home">
                  <button
                    class="pf-v6-c-button pf-m-circle pf-m-plain"
                    type="button"
                    aria-label="Home"
                  >
                    <span class="pf-v6-c-button__icon">
                      <svg
                        class="pf-v6-svg"
                        viewBox="0 0 32 32"
                        fill="currentColor"
                        aria-hidden="true"
                        role="img"
                        width="1em"
                        height="1em"
                      >
                        <path
                          d="M30.707 15.435 17.061 1.789a1.501 1.501 0 0 0-2.121 0L1.293 15.435a.999.999 0 1 0 1.414 1.414L3 16.556V29.5c0 .827.673 1.5 1.5 1.5h23c.827 0 1.5-.673 1.5-1.5V16.556l.293.293a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414ZM19 29h-6V19h6v10Zm8-10v10h-6V18.5c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5V29H5V14.556l11-11 11 11V19Z"
                        />
                      </svg>
                    </span>
                  </button>
                </div>
                <div class="pf-v6-c-compass__nav-main">
                  <nav
                    class="pf-v6-c-tabs pf-m-nav"
                    aria-label="Compass primary"
                  >
                    <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
                      <button
                        class="pf-v6-c-button pf-m-small pf-m-plain"
                        type="button"
                        aria-label="Scroll left"
                        disabled
                      >
                        <span class="pf-v6-c-button__icon">
                          <svg
                            class="pf-v6-svg"
                            viewBox="0 0 20 20"
                            fill="currentColor"
                            aria-hidden="true"
                            role="img"
                            width="1em"
                            height="1em"
                          >
                            <path
                              d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                            />
                          </svg>
                        </span>
                      </button>
                    </div>
                    <ul
                      class="pf-v6-c-tabs__list"
                      role="tablist"
                      aria-label="Compass primary"
                    >
                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="primary-nav-users-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Users</span>
                        </a>
                      </li>
                      <li
                        class="pf-v6-c-tabs__item pf-m-current"
                        role="presentation"
                      >
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="true"
                          id="primary-nav-containers-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Containers</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="primary-nav-database-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Database</span>
                        </a>
                      </li>

                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="primary-nav-server-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Server</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="primary-nav-system-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">System</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="primary-nav-network-wired-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Network</span>
                        </a>
                      </li>
                    </ul>

                    <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
                      <button
                        class="pf-v6-c-button pf-m-small pf-m-plain"
                        type="button"
                        aria-label="Scroll right"
                        disabled
                      >
                        <span class="pf-v6-c-button__icon">
                          <svg
                            class="pf-v6-svg"
                            viewBox="0 0 20 20"
                            fill="currentColor"
                            aria-hidden="true"
                            role="img"
                            width="1em"
                            height="1em"
                          >
                            <path
                              d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                            />
                          </svg>
                        </span>
                      </button>
                    </div>
                  </nav>
                </div>
                <div class="pf-v6-c-compass__nav-search">
                  <button
                    class="pf-v6-c-button pf-m-circle pf-m-plain"
                    type="button"
                    aria-label="Search"
                  >
                    <span class="pf-v6-c-button__icon">
                      <svg
                        class="pf-v6-svg"
                        viewBox="0 0 32 32"
                        fill="currentColor"
                        aria-hidden="true"
                        role="img"
                        width="1em"
                        height="1em"
                      >
                        <path
                          d="m30.796 29.205-8.557-8.557A11.945 11.945 0 0 0 25 13c0-6.617-5.383-12-12-12S1 6.383 1 13s5.383 12 12 12c2.904 0 5.57-1.038 7.648-2.761l8.556 8.556a1.122 1.122 0 0 0 1.592 0 1.127 1.127 0 0 0 0-1.591ZM3 13C3 7.486 7.486 3 13 3s10 4.486 10 10-4.486 10-10 10S3 18.514 3 13Z"
                        />
                      </svg>
                    </span>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="pf-v6-c-panel pf-m-pill pf-m-glass">
          <div class="pf-v6-c-panel__main">
            <div class="pf-v6-c-panel__main-body">
              <div class="pf-v6-c-compass__nav-content">
                <div class="pf-v6-c-compass__nav-main">
                  <nav
                    class="pf-v6-c-tabs pf-m-nav pf-m-subtab"
                    aria-label="Compass secondary"
                  >
                    <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
                      <button
                        class="pf-v6-c-button pf-m-small pf-m-plain"
                        type="button"
                        aria-label="Scroll left"
                        disabled
                      >
                        <span class="pf-v6-c-button__icon">
                          <svg
                            class="pf-v6-svg"
                            viewBox="0 0 20 20"
                            fill="currentColor"
                            aria-hidden="true"
                            role="img"
                            width="1em"
                            height="1em"
                          >
                            <path
                              d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                            />
                          </svg>
                        </span>
                      </button>
                    </div>
                    <ul
                      class="pf-v6-c-tabs__list"
                      role="tablist"
                      aria-label="Compass secondary"
                    >
                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="secondary-nav-sub-1-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Item 1</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="secondary-nav-sub-2-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Item 2</span>
                        </a>
                      </li>
                      <li
                        class="pf-v6-c-tabs__item pf-m-current"
                        role="presentation"
                      >
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="true"
                          id="secondary-nav-sub-3-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Item 3</span>
                        </a>
                      </li>

                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link pf-m-disabled"
                          aria-disabled="true"
                          tabindex="-1"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="secondary-nav-sub-disabled-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Disabled</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link pf-m-aria-disabled"
                          aria-disabled="true"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="secondary-nav-sub-aria-disabled-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="secondary-nav-sub-6-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Item 6</span>
                        </a>
                      </li>
                    </ul>

                    <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
                      <button
                        class="pf-v6-c-button pf-m-small pf-m-plain"
                        type="button"
                        aria-label="Scroll right"
                        disabled
                      >
                        <span class="pf-v6-c-button__icon">
                          <svg
                            class="pf-v6-svg"
                            viewBox="0 0 20 20"
                            fill="currentColor"
                            aria-hidden="true"
                            role="img"
                            width="1em"
                            height="1em"
                          >
                            <path
                              d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                            />
                          </svg>
                        </span>
                      </button>
                    </div>
                  </nav>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-compass__profile">
        <button
          class="pf-v6-c-menu-toggle pf-m-circle pf-m-text pf-m-plain"
          type="button"
          aria-expanded="false"
        >
          <span class="pf-v6-c-menu-toggle__icon">
            <img
              class="pf-v6-c-avatar pf-m-md"
              alt="Avatar image"
              src="/assets/images/img_avatar-light.svg"
            />
          </span>
          <span class="pf-v6-c-menu-toggle__text">Ned Username</span>
          <span class="pf-v6-c-menu-toggle__controls">
            <span class="pf-v6-c-menu-toggle__toggle-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </div>
    </div>
    <div class="pf-v6-c-compass__sidebar pf-m-expanded pf-m-start">
      <div class="pf-v6-c-panel pf-m-pill pf-m-glass">
        <div class="pf-v6-c-panel__main">
          <div class="pf-v6-c-panel__main-body">
            <div class="pf-v6-c-action-list pf-m-icons pf-m-vertical">
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="Add"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M28.5 2h-25C2.673 2 2 2.673 2 3.5v25c0 .827.673 1.5 1.5 1.5h25c.827 0 1.5-.673 1.5-1.5v-25c0-.827-.673-1.5-1.5-1.5ZM28 28H4V4h24v24ZM8 16a1 1 0 0 1 1-1h6V9a1 1 0 1 1 2 0v6h6a1 1 0 1 1 0 2h-6v6a1 1 0 1 1-2 0v-6H9a1 1 0 0 1-1-1Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="Collections"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M28.5 11h-25c-.827 0-1.5.673-1.5 1.5v17c0 .827.673 1.5 1.5 1.5h25c.827 0 1.5-.673 1.5-1.5v-17c0-.827-.673-1.5-1.5-1.5ZM28 29H4V13h24v16ZM6 2a1 1 0 0 1 1-1h18a1 1 0 0 1 0 2H7a1 1 0 0 1-1-1ZM4 7a1 1 0 0 1 1-1h22a1 1 0 0 1 0 2H5a1 1 0 0 1-1-1Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-v6-m-ai-indicator pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="AI assistant"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M30.502 7c0 .29-.209.536-.498.59a5.523 5.523 0 0 0-4.417 4.417c-.054.289-.3.498-.59.498s-.536-.21-.59-.498A5.52 5.52 0 0 0 19.99 7.59c-.289-.054-.498-.3-.498-.59s.21-.536.498-.59a5.52 5.52 0 0 0 4.417-4.417c.054-.289.301-.498.59-.498s.536.21.59.498a5.523 5.523 0 0 0 4.417 4.417c.289.054.498.3.498.59Zm-4.465 9.962A11.932 11.932 0 0 1 15.038 5.97C15.001 5.447 14.524 5 14 5c-.521 0-.997.442-1.038.962a11.932 11.932 0 0 1-10.992 11C1.447 16.999 1 17.476 1 18c0 .521.442.997.962 1.038a11.932 11.932 0 0 1 11 10.992c.037.524.514.97 1.038.97.521 0 .997-.442 1.038-.962a11.933 11.933 0 0 1 11-10.999c.519-.042.961-.516.961-1.038 0-.521-.442-.997-.962-1.038Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="Volume"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M17.439 2.102a1 1 0 0 0-1.054.109L7.656 9H2.5C1.673 9 1 9.673 1 10.5v11c0 .827.673 1.5 1.5 1.5h5.157l8.729 6.789a.998.998 0 0 0 1.053.109c.343-.168.561-.517.561-.898V3a1 1 0 0 0-.561-.898ZM16 26.955l-7.386-5.744A1 1 0 0 0 8 21H3V11h5a.997.997 0 0 0 .614-.211L16 5.045v21.91ZM31 16a14.94 14.94 0 0 1-4.284 10.488.997.997 0 0 1-1.414.018 1 1 0 0 1-.018-1.414C27.68 22.637 29 19.408 29 16s-1.319-6.637-3.716-9.092a.999.999 0 1 1 1.432-1.396A14.94 14.94 0 0 1 31 16Zm-6 0a9.007 9.007 0 0 1-2.249 5.95.996.996 0 0 1-1.411.091 1 1 0 0 1-.091-1.411C22.378 19.346 23 17.702 23 16s-.622-3.346-1.751-4.63a1 1 0 0 1 1.502-1.32A9.007 9.007 0 0 1 25 16Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="Use microphone"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M16 22c3.86 0 7-3.141 7-7V8c0-3.859-3.14-7-7-7S9 4.141 9 8v7c0 3.859 3.14 7 7 7ZM11 8c0-2.757 2.243-5 5-5s5 2.243 5 5v7c0 2.757-2.243 5-5 5s-5-2.243-5-5V8Zm5.99 17.95c0 .018.01.032.01.05v2.021h5a1 1 0 1 1 0 2H10.02a1 1 0 1 1 0-2H15V26c0-.018.009-.033.01-.05C9.407 25.447 5 20.731 5 15a1 1 0 1 1 2 0c0 4.963 4.038 9 9 9s9-4.037 9-9a1 1 0 1 1 2 0c0 5.731-4.407 10.447-10.01 10.95Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="pf-v6-c-compass__main">
      <div class="pf-v6-c-compass__main-header">
        <div class="pf-v6-c-panel pf-m-glass">
          <div class="pf-v6-c-panel__main">
            <div class="pf-v6-c-panel__main-body">
              <div class="pf-v6-c-compass__main-header-content">
                <div class="pf-v6-c-compass__main-header-title">
                  <h2 class="pf-v6-c-title pf-m-h1">Page title</h2>
                </div>
                <div class="pf-v6-c-compass__main-header-toolbar">
                  <div class="pf-v6-c-action-list">
                    <div class="pf-v6-c-action-list__group">
                      <div class="pf-v6-c-action-list__item">
                        <button
                          class="pf-v6-c-button pf-m-primary"
                          type="button"
                        >
                          <span class="pf-v6-c-button__text">Add integration</span>
                        </button>
                      </div>
                      <div class="pf-v6-c-action-list__item">
                        <button
                          class="pf-v6-c-button pf-m-secondary"
                          type="button"
                        >
                          <span class="pf-v6-c-button__text">Test integration</span>
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-compass__content">
        <div
          class="pf-v6-c-panel pf-m-glass pf-m-scrollable-auto-height pf-m-scrollable"
        >
          <div class="pf-v6-c-panel__main">
            <div class="pf-v6-c-panel__main-body">
              <div class="pf-v6-l-flex pf-m-column pf-m-gap-md">
                <div class="pf-v6-c-toolbar" id="-toolbar">
                  <div class="pf-v6-c-toolbar__content">
                    <div class="pf-v6-c-toolbar__content-section pf-m-nowrap">
                      <div
                        class="pf-v6-c-toolbar__group pf-m-show-on-xl pf-m-toggle-group"
                      >
                        <div class="pf-v6-c-toolbar__toggle">
                          <button
                            class="pf-v6-c-menu-toggle pf-m-plain"
                            type="button"
                            aria-expanded="false"
                            aria-label="Show filters"
                            aria-controls="-toolbar-expandable-content"
                          >
                            <span class="pf-v6-c-menu-toggle__icon">
                              <svg
                                class="pf-v6-svg"
                                viewBox="0 0 32 32"
                                fill="currentColor"
                                aria-hidden="true"
                                role="img"
                                width="1em"
                                height="1em"
                              >
                                <path
                                  d="M29.875 3.5V7a.876.876 0 0 1-.256.619l-9.744 9.744v10.638a.875.875 0 0 1-.599.83l-6 2a.876.876 0 0 1-.788-.12.874.874 0 0 1-.363-.71V17.363L2.381 7.619A.876.876 0 0 1 2.125 7V3.5c0-.758.617-1.375 1.375-1.375h25c.758 0 1.375.617 1.375 1.375Z"
                                />
                              </svg>
                            </span>
                          </button>
                        </div>
                        <div class="pf-v6-c-toolbar__item pf-m-bulk-select">
                          <div
                            class="pf-v6-c-menu-toggle pf-m-split-button"
                            id="-toolbar-check"
                          >
                            <label
                              class="pf-v6-c-check pf-m-standalone"
                              for="-toolbar-check-check-input"
                            >
                              <input
                                class="pf-v6-c-check__input"
                                type="checkbox"
                                id="-toolbar-check-check-input"
                                name="-toolbar-check-check-input"
                                aria-label="Standalone check"
                              />
                            </label>
                            <button
                              class="pf-v6-c-menu-toggle__button"
                              type="button"
                              aria-expanded="false"
                              id="-toolbar-menu-toggle-toggle-button"
                              aria-label="Menu toggle"
                            >
                              <span class="pf-v6-c-menu-toggle__controls">
                                <span class="pf-v6-c-menu-toggle__toggle-icon">
                                  <svg
                                    class="pf-v6-svg"
                                    viewBox="0 0 20 20"
                                    fill="currentColor"
                                    aria-hidden="true"
                                    role="img"
                                    width="1em"
                                    height="1em"
                                  >
                                    <path
                                      d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
                                    />
                                  </svg>
                                </span>
                              </span>
                            </button>
                          </div>
                        </div>

                        <div class="pf-v6-c-toolbar__item">
                          <button
                            class="pf-v6-c-menu-toggle"
                            type="button"
                            aria-expanded="false"
                            id="-toolbar-select-checkbox-status"
                          >
                            <span class="pf-v6-c-menu-toggle__text">Status</span>
                            <span class="pf-v6-c-menu-toggle__controls">
                              <span class="pf-v6-c-menu-toggle__toggle-icon">
                                <svg
                                  class="pf-v6-svg"
                                  viewBox="0 0 20 20"
                                  fill="currentColor"
                                  aria-hidden="true"
                                  role="img"
                                  width="1em"
                                  height="1em"
                                >
                                  <path
                                    d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
                                  />
                                </svg>
                              </span>
                            </span>
                          </button>
                        </div>
                      </div>

                      <div
                        class="pf-v6-c-overflow-menu"
                        id="-toolbar-overflow-menu"
                      >
                        <div
                          class="pf-v6-c-overflow-menu__content pf-v6-u-display-none pf-v6-u-display-flex-on-lg"
                        >
                          <div
                            class="pf-v6-c-overflow-menu__group pf-m-button-group"
                          >
                            <div class="pf-v6-c-overflow-menu__item">
                              <button
                                class="pf-v6-c-button pf-m-primary"
                                type="button"
                              >
                                <span
                                  class="pf-v6-c-button__text"
                                >Create instance</span>
                              </button>
                            </div>
                          </div>
                        </div>
                        <div class="pf-v6-c-overflow-menu__control">
                          <button
                            class="pf-v6-c-menu-toggle pf-m-plain"
                            type="button"
                            aria-expanded="false"
                            aria-label="Menu toggle"
                            id="-toolbar-overflow-menu-toggle"
                          >
                            <span class="pf-v6-c-menu-toggle__icon">
                              <svg
                                class="pf-v6-svg"
                                viewBox="0 0 32 32"
                                fill="currentColor"
                                aria-hidden="true"
                                role="img"
                                width="1em"
                                height="1em"
                              >
                                <path
                                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                />
                              </svg>
                            </span>
                          </button>
                        </div>
                      </div>

                      <div class="pf-v6-c-toolbar__item pf-m-pagination">
                        <div class="pf-v6-c-pagination pf-m-compact">
                          <div class="pf-v6-c-pagination__page-menu">
                            <button
                              class="pf-v6-c-menu-toggle pf-m-text pf-m-plain"
                              type="button"
                              aria-expanded="false"
                              id="-toolbar-top-pagination"
                            >
                              <span class="pf-v6-c-menu-toggle__text">
                                <b>1 - 10</b>&nbsp;of&nbsp;
                                <b>36</b>
                              </span>
                              <span class="pf-v6-c-menu-toggle__controls">
                                <span class="pf-v6-c-menu-toggle__toggle-icon">
                                  <svg
                                    class="pf-v6-svg"
                                    viewBox="0 0 20 20"
                                    fill="currentColor"
                                    aria-hidden="true"
                                    role="img"
                                    width="1em"
                                    height="1em"
                                  >
                                    <path
                                      d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
                                    />
                                  </svg>
                                </span>
                              </span>
                            </button>
                          </div>
                          <nav
                            class="pf-v6-c-pagination__nav"
                            aria-label="Toolbar top pagination"
                          >
                            <div
                              class="pf-v6-c-pagination__nav-control pf-m-prev"
                            >
                              <button
                                class="pf-v6-c-button pf-m-plain"
                                type="button"
                                disabled
                                aria-label="Go to previous page"
                              >
                                <span class="pf-v6-c-button__icon">
                                  <svg
                                    class="pf-v6-svg"
                                    viewBox="0 0 256 512"
                                    fill="currentColor"
                                    aria-hidden="true"
                                    role="img"
                                    width="1em"
                                    height="1em"
                                  >
                                    <path
                                      d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
                                    />
                                  </svg>
                                </span>
                              </button>
                            </div>
                            <div
                              class="pf-v6-c-pagination__nav-control pf-m-next"
                            >
                              <button
                                class="pf-v6-c-button pf-m-plain"
                                type="button"
                                aria-label="Go to next page"
                              >
                                <span class="pf-v6-c-button__icon">
                                  <svg
                                    class="pf-v6-svg"
                                    viewBox="0 0 256 512"
                                    fill="currentColor"
                                    aria-hidden="true"
                                    role="img"
                                    width="1em"
                                    height="1em"
                                  >
                                    <path
                                      d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
                                    />
                                  </svg>
                                </span>
                              </button>
                            </div>
                          </nav>
                        </div>
                      </div>
                    </div>

                    <div
                      class="pf-v6-c-toolbar__expandable-content pf-m-hidden"
                      id="-toolbar-expandable-content"
                      hidden
                    ></div>
                  </div>
                </div>
                <div class="pf-v6-l-gallery pf-m-gutter">
                  <div
                    class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                    id="card-view-basic-example-gallery-card-empty-state"
                  >
                    <div class="pf-v6-l-bullseye">
                      <div class="pf-v6-c-empty-state pf-m-xs">
                        <div class="pf-v6-c-empty-state__content">
                          <div class="pf-v6-c-empty-state__icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7 16.125h-5.875V23a1.125 1.125 0 0 1-2.25 0v-5.875H9a1.125 1.125 0 0 1 0-2.25h5.875V9a1.125 1.125 0 0 1 2.25 0v5.875H23a1.125 1.125 0 0 1 0 2.25Z"
                              />
                            </svg>
                          </div>
                          <div class="pf-v6-c-card__title">
                            <h2
                              class="pf-v6-c-card__title-text pf-m-md"
                            >Add a new card to your page</h2>
                          </div>
                          <button
                            class="pf-v6-c-button pf-m-link"
                            type="button"
                          >
                            <span class="pf-v6-c-button__text">Add card</span>
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div
                    class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                    id="card-view-basic-example-gallery-card-1"
                  >
                    <div class="pf-v6-c-card__header">
                      <img
                        src="/assets/images/PF-IconLogo.svg"
                        alt="PatternFly logo"
                      />
                      <div class="pf-v6-c-card__actions">
                        <button
                          class="pf-v6-c-menu-toggle pf-m-plain"
                          type="button"
                          aria-expanded="false"
                          aria-label="Menu toggle"
                          id="card-view-basic-example-gallery-card-1-toggle"
                        >
                          <span class="pf-v6-c-menu-toggle__icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                              />
                            </svg>
                          </span>
                        </button>
                        <div class="pf-v6-c-check pf-m-standalone">
                          <input
                            class="pf-v6-c-check__input"
                            type="checkbox"
                            id="card-view-basic-example-gallery-card-1-check"
                            name="card-view-basic-example-gallery-card-1-check"
                            aria-labelledby="card-view-basic-example-gallery-card-1-check-label"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="pf-v6-c-card__title">
                      <h2
                        class="pf-v6-c-card__title-text"
                        id="card-view-basic-example-gallery-card-1-check-label"
                      >Patternfly</h2>
                      <div class="pf-v6-c-content">
                        <small>Provided by Red Hat</small>
                      </div>
                    </div>
                    <div
                      class="pf-v6-c-card__body"
                    >PatternFly is a community project that promotes design commonality and improves user experience.</div>
                  </div>
                  <div
                    class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                    id="card-view-basic-example-gallery-card-2"
                  >
                    <div class="pf-v6-c-card__header">
                      <img
                        src="/assets/images/activemq-core_200x150.png"
                        width="60px"
                        alt="Logo"
                      />
                      <div class="pf-v6-c-card__actions">
                        <button
                          class="pf-v6-c-menu-toggle pf-m-plain"
                          type="button"
                          aria-expanded="false"
                          aria-label="Menu toggle"
                          id="card-view-basic-example-gallery-card-2-toggle"
                        >
                          <span class="pf-v6-c-menu-toggle__icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                              />
                            </svg>
                          </span>
                        </button>
                        <div class="pf-v6-c-check pf-m-standalone">
                          <input
                            class="pf-v6-c-check__input"
                            type="checkbox"
                            id="card-view-basic-example-gallery-card-2-check"
                            name="card-view-basic-example-gallery-card-2-check"
                            aria-labelledby="card-view-basic-example-gallery-card-2-check-label"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="pf-v6-c-card__title">
                      <h2
                        class="pf-v6-c-card__title-text"
                        id="card-view-basic-example-gallery-card-2-check-label"
                      >ActiveMq</h2>
                      <div class="pf-v6-c-content">
                        <small>Provided by Red Hat</small>
                      </div>
                    </div>
                    <div
                      class="pf-v6-c-card__body"
                    >The ActiveMQ component allows messages to be sent to a JMS Queue or Topic; or messages to be consumed from a JMS Queue or Topic using Apache ActiveMQ.</div>
                  </div>
                  <div
                    class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                    id="card-view-basic-example-gallery-card-3"
                  >
                    <div class="pf-v6-c-card__header">
                      <img
                        src="/assets/images/camel-spark_200x150.png"
                        width="60px"
                        alt="Logo"
                      />
                      <div class="pf-v6-c-card__actions">
                        <button
                          class="pf-v6-c-menu-toggle pf-m-plain"
                          type="button"
                          aria-expanded="false"
                          aria-label="Menu toggle"
                          id="card-view-basic-example-gallery-card-3-toggle"
                        >
                          <span class="pf-v6-c-menu-toggle__icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                              />
                            </svg>
                          </span>
                        </button>
                        <div class="pf-v6-c-check pf-m-standalone">
                          <input
                            class="pf-v6-c-check__input"
                            type="checkbox"
                            id="card-view-basic-example-gallery-card-3-check"
                            name="card-view-basic-example-gallery-card-3-check"
                            aria-labelledby="card-view-basic-example-gallery-card-3-check-label"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="pf-v6-c-card__title">
                      <h2
                        class="pf-v6-c-card__title-text"
                        id="card-view-basic-example-gallery-card-3-check-label"
                      >Apache Spark</h2>
                      <div class="pf-v6-c-content">
                        <small>Provided by Red Hat</small>
                      </div>
                    </div>
                    <div
                      class="pf-v6-c-card__body"
                    >This documentation page covers the Apache Spark component for the Apache Camel.</div>
                  </div>
                  <div
                    class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                    id="card-view-basic-example-gallery-card-4"
                  >
                    <div class="pf-v6-c-card__header">
                      <img
                        src="/assets/images/camel-avro_200x150.png"
                        width="60px"
                        alt="Logo"
                      />
                      <div class="pf-v6-c-card__actions">
                        <button
                          class="pf-v6-c-menu-toggle pf-m-plain"
                          type="button"
                          aria-expanded="false"
                          aria-label="Menu toggle"
                          id="card-view-basic-example-gallery-card-4-toggle"
                        >
                          <span class="pf-v6-c-menu-toggle__icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                              />
                            </svg>
                          </span>
                        </button>
                        <div class="pf-v6-c-check pf-m-standalone">
                          <input
                            class="pf-v6-c-check__input"
                            type="checkbox"
                            id="card-view-basic-example-gallery-card-4-check"
                            name="card-view-basic-example-gallery-card-4-check"
                            aria-labelledby="card-view-basic-example-gallery-card-4-check-label"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="pf-v6-c-card__title">
                      <h2
                        class="pf-v6-c-card__title-text"
                        id="card-view-basic-example-gallery-card-4-check-label"
                      >Avro</h2>
                      <div class="pf-v6-c-content">
                        <small>Provided by Red Hat</small>
                      </div>
                    </div>
                    <div
                      class="pf-v6-c-card__body"
                    >This component provides a dataformat for avro, which allows serialization and deserialization of messages using Apache Avro’s binary dataformat. Moreover, it provides support for Apache Avro’s rpc, by providing producers and consumers endpoint for using avro over netty or http.</div>
                  </div>
                  <div
                    class="pf-v6-c-card pf-m-selectable-raised pf-m-selected-raised pf-m-compact"
                    id="card-view-basic-example-gallery-card-5"
                  >
                    <div class="pf-v6-c-card__header">
                      <img
                        src="/assets/images/FuseConnector_Icons_AzureServices.png"
                        width="60px"
                        alt="Logo"
                      />
                      <div class="pf-v6-c-card__actions">
                        <button
                          class="pf-v6-c-menu-toggle pf-m-plain"
                          type="button"
                          aria-expanded="false"
                          aria-label="Menu toggle"
                          id="card-view-basic-example-gallery-card-5-toggle"
                        >
                          <span class="pf-v6-c-menu-toggle__icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                              />
                            </svg>
                          </span>
                        </button>
                        <div class="pf-v6-c-check pf-m-standalone">
                          <input
                            class="pf-v6-c-check__input"
                            type="checkbox"
                            id="card-view-basic-example-gallery-card-5-check"
                            name="card-view-basic-example-gallery-card-5-check"
                            aria-labelledby="card-view-basic-example-gallery-card-5-check-label"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="pf-v6-c-card__title">
                      <h2
                        class="pf-v6-c-card__title-text"
                        id="card-view-basic-example-gallery-card-5-check-label"
                      >Azure Services</h2>
                      <div class="pf-v6-c-content">
                        <small>Provided by Red Hat</small>
                      </div>
                    </div>
                    <div
                      class="pf-v6-c-card__body"
                    >The Camel Components for Windows Azure Services provide connectivity to Azure services from Camel.</div>
                  </div>
                  <div
                    class="pf-v6-c-card pf-m-non-selectable-raised pf-m-compact"
                    id="card-view-basic-example-gallery-card-6"
                  >
                    <div class="pf-v6-c-card__header">
                      <img
                        src="/assets/images/camel-saxon_200x150.png"
                        width="60px"
                        alt="Logo"
                      />
                      <div class="pf-v6-c-card__actions">
                        <button
                          class="pf-v6-c-menu-toggle pf-m-plain"
                          type="button"
                          aria-expanded="false"
                          aria-label="Menu toggle"
                          id="card-view-basic-example-gallery-card-6-toggle"
                        >
                          <span class="pf-v6-c-menu-toggle__icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                              />
                            </svg>
                          </span>
                        </button>
                        <div class="pf-v6-c-check pf-m-standalone">
                          <input
                            class="pf-v6-c-check__input"
                            type="checkbox"
                            id="card-view-basic-example-gallery-card-6-check"
                            name="card-view-basic-example-gallery-card-6-check"
                            disabled
                            aria-labelledby="card-view-basic-example-gallery-card-6-check-label"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="pf-v6-c-card__title">
                      <h2
                        class="pf-v6-c-card__title-text"
                        id="card-view-basic-example-gallery-card-6-check-label"
                      >Crypto</h2>
                      <div class="pf-v6-c-content">
                        <small>Provided by Red Hat</small>
                      </div>
                    </div>
                    <div
                      class="pf-v6-c-card__body"
                    >For providing flexible endpoints to sign and verify exchanges using the Signature Service of the Java Cryptographic Extension.</div>
                  </div>
                  <div
                    class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                    id="card-view-basic-example-gallery-card-7"
                  >
                    <div class="pf-v6-c-card__header">
                      <img
                        src="/assets/images/camel-dropbox_200x150.png"
                        width="60px"
                        alt="Logo"
                      />
                      <div class="pf-v6-c-card__actions">
                        <button
                          class="pf-v6-c-menu-toggle pf-m-plain"
                          type="button"
                          aria-expanded="false"
                          aria-label="Menu toggle"
                          id="card-view-basic-example-gallery-card-7-toggle"
                        >
                          <span class="pf-v6-c-menu-toggle__icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                              />
                            </svg>
                          </span>
                        </button>
                        <div class="pf-v6-c-check pf-m-standalone">
                          <input
                            class="pf-v6-c-check__input"
                            type="checkbox"
                            id="card-view-basic-example-gallery-card-7-check"
                            name="card-view-basic-example-gallery-card-7-check"
                            aria-labelledby="card-view-basic-example-gallery-card-7-check-label"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="pf-v6-c-card__title">
                      <h2
                        class="pf-v6-c-card__title-text"
                        id="card-view-basic-example-gallery-card-7-check-label"
                      >DropBox</h2>
                      <div class="pf-v6-c-content">
                        <small>Provided by Red Hat</small>
                      </div>
                    </div>
                    <div
                      class="pf-v6-c-card__body"
                    >The dropbox: component allows you to treat Dropbox remote folders as a producer or consumer of messages.</div>
                  </div>
                  <div
                    class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                    id="card-view-basic-example-gallery-card-8"
                  >
                    <div class="pf-v6-c-card__header">
                      <img
                        src="/assets/images/camel-infinispan_200x150.png"
                        width="60px"
                        alt="Logo"
                      />
                      <div class="pf-v6-c-card__actions">
                        <button
                          class="pf-v6-c-menu-toggle pf-m-plain"
                          type="button"
                          aria-expanded="false"
                          aria-label="Menu toggle"
                          id="card-view-basic-example-gallery-card-8-toggle"
                        >
                          <span class="pf-v6-c-menu-toggle__icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                              />
                            </svg>
                          </span>
                        </button>
                        <div class="pf-v6-c-check pf-m-standalone">
                          <input
                            class="pf-v6-c-check__input"
                            type="checkbox"
                            id="card-view-basic-example-gallery-card-8-check"
                            name="card-view-basic-example-gallery-card-8-check"
                            aria-labelledby="card-view-basic-example-gallery-card-8-check-label"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="pf-v6-c-card__title">
                      <h2
                        class="pf-v6-c-card__title-text"
                        id="card-view-basic-example-gallery-card-8-check-label"
                      >JBoss Data Grid</h2>
                      <div class="pf-v6-c-content">
                        <small>Provided by Red Hat</small>
                      </div>
                    </div>
                    <div
                      class="pf-v6-c-card__body"
                    >Read or write to a fully-supported distributed cache and data grid for faster integration services.</div>
                  </div>
                  <div
                    class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                    id="card-view-basic-example-gallery-card-9"
                  >
                    <div class="pf-v6-c-card__header">
                      <img
                        src="/assets/images/FuseConnector_Icons_REST.png"
                        width="60px"
                        alt="Logo"
                      />
                      <div class="pf-v6-c-card__actions">
                        <button
                          class="pf-v6-c-menu-toggle pf-m-plain"
                          type="button"
                          aria-expanded="false"
                          aria-label="Menu toggle"
                          id="card-view-basic-example-gallery-card-9-toggle"
                        >
                          <span class="pf-v6-c-menu-toggle__icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                              />
                            </svg>
                          </span>
                        </button>
                        <div class="pf-v6-c-check pf-m-standalone">
                          <input
                            class="pf-v6-c-check__input"
                            type="checkbox"
                            id="card-view-basic-example-gallery-card-9-check"
                            name="card-view-basic-example-gallery-card-9-check"
                            aria-labelledby="card-view-basic-example-gallery-card-9-check-label"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="pf-v6-c-card__title">
                      <h2
                        class="pf-v6-c-card__title-text"
                        id="card-view-basic-example-gallery-card-9-check-label"
                      >Rest</h2>
                      <div class="pf-v6-c-content">
                        <small>Provided by Red Hat</small>
                      </div>
                    </div>
                    <div class="pf-v6-c-card__body">
                      The rest component allows to define REST endpoints (consumer) using the Rest DSL and plugin to other Camel components as the REST transport.
                      From Camel 2.18 onwards the rest component can also be used as a client (producer) to call REST services.
                    </div>
                  </div>
                  <div
                    class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                    id="card-view-basic-example-gallery-card-10"
                  >
                    <div class="pf-v6-c-card__header">
                      <img
                        src="/assets/images/camel-swagger-java_200x150.png"
                        width="60px"
                        alt="Logo"
                      />
                      <div class="pf-v6-c-card__actions">
                        <button
                          class="pf-v6-c-menu-toggle pf-m-plain"
                          type="button"
                          aria-expanded="false"
                          aria-label="Menu toggle"
                          id="card-view-basic-example-gallery-card-10-toggle"
                        >
                          <span class="pf-v6-c-menu-toggle__icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                              />
                            </svg>
                          </span>
                        </button>
                        <div class="pf-v6-c-check pf-m-standalone">
                          <input
                            class="pf-v6-c-check__input"
                            type="checkbox"
                            id="card-view-basic-example-gallery-card-10-check"
                            name="card-view-basic-example-gallery-card-10-check"
                            aria-labelledby="card-view-basic-example-gallery-card-10-check-label"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="pf-v6-c-card__title">
                      <h2
                        class="pf-v6-c-card__title-text"
                        id="card-view-basic-example-gallery-card-10-check-label"
                      >SWAGGER</h2>
                      <div class="pf-v6-c-content">
                        <small>Provided by Red Hat</small>
                      </div>
                    </div>
                    <div
                      class="pf-v6-c-card__body"
                    >Expose REST services and their APIs using Swagger specification.</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-compass__main-footer pf-m-expanded">
        <div class="pf-v6-c-compass__message-bar">
          <div class="pf-v6-c-panel pf-m-pill pf-m-glass pf-m-no-border">
            <div class="pf-v6-c-panel__main">chatbot message bar</div>
          </div>
        </div>
      </div>
    </div>
    <div class="pf-v6-c-compass__sidebar pf-m-expanded pf-m-end">
      <div class="pf-v6-c-panel pf-m-pill pf-m-glass">
        <div class="pf-v6-c-panel__main">
          <div class="pf-v6-c-panel__main-body">
            <div class="pf-v6-c-action-list pf-m-icons pf-m-vertical">
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="Notifications"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M28 21c-1.103 0-2-.897-2-2v-4c0-4.885-3.523-8.955-8.159-9.823.405-.445.659-1.03.659-1.677C18.5 2.122 17.379 1 16 1s-2.5 1.122-2.5 2.5c0 .647.254 1.233.659 1.677C9.523 6.045 6 10.115 6 15v4c0 1.103-.897 2-2 2a1 1 0 0 0-1 1v3.5c0 .827.673 1.5 1.5 1.5H12c0 2.206 1.794 4 4 4s4-1.794 4-4h7.5c.827 0 1.5-.673 1.5-1.5V22a1 1 0 0 0-1-1Zm-1 4H5v-2.126A4.006 4.006 0 0 0 8 19v-4c0-4.411 3.589-8 8-8s8 3.589 8 8v4a4.008 4.008 0 0 0 3 3.874V25Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="List"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M31 16a1 1 0 0 1-1 1H9a1 1 0 0 1 0-2h21a1 1 0 0 1 1 1Zm-1 9H9a1 1 0 0 0 0 2h21a1 1 0 0 0 0-2ZM9 7h21a1 1 0 0 0 0-2H9a1 1 0 0 0 0 2ZM2 4.51a1.5 1.5 0 1 0 .001 3.001A1.5 1.5 0 0 0 2 4.51Zm0 10a1.5 1.5 0 1 0 .001 3.001A1.5 1.5 0 0 0 2 14.51Zm0 10a1.5 1.5 0 1 0 .001 3.001A1.5 1.5 0 0 0 2 24.51Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="Zap"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M15 31a1 1 0 0 1-1-1V19h-4a.999.999 0 0 1-.916-1.401l7-16A1 1 0 0 1 18 2v11h4a.999.999 0 0 1 .916 1.401l-7 16A.998.998 0 0 1 15 31Zm-3.471-14H14.5c.827 0 1.5.673 1.5 1.5v6.719L20.471 15H17.5c-.827 0-1.5-.673-1.5-1.5V6.781L11.529 17Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="Download"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M30 29a1 1 0 0 1-1 1H3a1 1 0 0 1 0-2h26a1 1 0 0 1 1 1Zm-15.061-4.646c.292.292.676.438 1.061.438s.768-.146 1.061-.438l8.646-8.646a.999.999 0 1 0-1.414-1.414L17 21.587V3a1 1 0 0 0-2 0v18.586l-7.293-7.293a.999.999 0 1 0-1.414 1.414l8.646 8.646Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="Help"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

```

### Dashboard

This demo populates the main Compass section with a dashboard, which is often used as the landing page within a Compass layout. This demo page includes:

* A `.pf-v6-c-hero` component positioned between the top navigation and the main page content, containing promotional or introductory content with important CTAs.
* A `.pf-v6-c-compass__content` without a glass panel component wrapping all of the contents. This removes the rounded-rectangle container that typically serves as the main content background. Instead, the content area is a dashboard (a grid of cards), and each card has a glass modifier.

```html isFullscreen isBeta
<div class="pf-v6-c-compass pf-m-animate-smoothly">
  <div class="pf-v6-c-compass__container">
    <div class="pf-v6-c-compass__header pf-m-expanded">
      <div class="pf-v6-c-compass__logo">
        <svg
          width="192"
          height="39"
          viewBox="0 0 192 39"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          aria-hidden="true"
        >
          <path
            d="M33.3807 22.9001C36.6672 22.9001 41.4287 22.2167 41.4287 18.2926C41.4287 17.9865 41.4209 17.6883 41.3472 17.3901L39.3885 8.85069C38.9336 6.97444 38.5392 6.11944 35.2501 4.47014C32.7023 3.16125 27.1468 1 25.5035 1C23.9733 1 23.5211 2.98972 21.7069 2.98972C19.8927 2.98972 18.6465 1.51194 17.0032 1.51194C15.3599 1.51194 14.395 2.59389 13.6036 4.81056C13.6036 4.81056 11.3924 11.0674 11.1085 11.9778C11.0506 12.1493 11.0506 12.3393 11.0506 12.4897C11.0506 14.9228 20.5921 22.9001 33.3833 22.9001M41.9414 19.8839C42.3963 22.0451 42.3963 22.2721 42.3963 22.5571C42.3963 26.2542 38.2579 28.3019 32.818 28.3019C20.5185 28.3019 9.74918 21.0767 9.74918 16.3003C9.74918 15.5614 9.92008 14.8779 10.1462 14.366C5.72383 14.5929 0 15.3899 0 20.4539C0 28.7585 19.6114 39 35.1396 39C47.0421 39 50.0447 33.5956 50.0447 29.3285C50.0447 25.9718 47.1552 22.1612 41.9388 19.8839"
            fill="#EE0000"
          />
          <path
            d="M41.9386 19.8864C42.3935 22.0477 42.3935 22.2746 42.3935 22.5596C42.3935 26.2567 38.255 28.3045 32.8152 28.3045C20.5157 28.3045 9.74634 21.0792 9.74634 16.3028C9.74634 15.5639 9.91724 14.8804 10.1434 14.3685L11.1083 11.9777C11.0504 12.1492 11.0504 12.3392 11.0504 12.4896C11.0504 14.9227 20.5919 22.9 33.3831 22.9C36.6696 22.9 41.4312 22.2165 41.4312 18.2925C41.4312 17.9864 41.4233 17.6882 41.3496 17.39L41.9412 19.8864H41.9386Z"
            fill="black"
          />
          <path
            d="M75.764 16V1.29995H82.295C83.261 1.29995 84.115 1.48895 84.857 1.86695C85.599 2.24495 86.173 2.76995 86.579 3.44195C86.999 4.09995 87.209 4.86995 87.209 5.75195C87.209 6.70395 86.943 7.53695 86.411 8.25095C85.893 8.95095 85.186 9.46195 84.29 9.78395L87.398 16H84.605L81.77 10.12H78.284V16H75.764ZM78.284 8.10395H82.064C82.848 8.10395 83.478 7.89395 83.954 7.47395C84.43 7.03995 84.668 6.47295 84.668 5.77295C84.668 5.05895 84.43 4.49195 83.954 4.07195C83.478 3.63795 82.848 3.42095 82.064 3.42095H78.284V8.10395Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M93.9392 16.21C92.9312 16.21 92.0212 15.972 91.2092 15.496C90.3972 15.006 89.7532 14.3549 89.2772 13.5429C88.8012 12.7169 88.5632 11.7859 88.5632 10.75C88.5632 9.71395 88.7872 8.78995 89.2352 7.97795C89.6832 7.16595 90.2922 6.52195 91.0622 6.04595C91.8462 5.55595 92.7142 5.31095 93.6662 5.31095C94.6462 5.31095 95.5072 5.54895 96.2492 6.02495C97.0052 6.50095 97.5932 7.14495 98.0132 7.95695C98.4472 8.76895 98.6642 9.69995 98.6642 10.75V11.3169H90.8942C90.9782 11.8909 91.1602 12.4019 91.4402 12.8499C91.7342 13.2839 92.1052 13.627 92.5532 13.879C93.0152 14.1309 93.5122 14.257 94.0442 14.257C94.5342 14.257 94.9962 14.173 95.4302 14.005C95.8782 13.823 96.2492 13.578 96.5432 13.2699L98.0972 14.677C97.4532 15.209 96.7952 15.601 96.1232 15.853C95.4652 16.091 94.7372 16.21 93.9392 16.21ZM90.9152 9.84695H96.4172C96.3332 9.34295 96.1582 8.89495 95.8922 8.50295C95.6402 8.11095 95.3182 7.80295 94.9262 7.57895C94.5482 7.35495 94.1282 7.24295 93.6662 7.24295C93.2042 7.24295 92.7772 7.35495 92.3852 7.57895C92.0072 7.78895 91.6922 8.08995 91.4402 8.48195C91.1882 8.87395 91.0132 9.32895 90.9152 9.84695Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M105.388 16.1049C104.506 16.1049 103.708 15.867 102.994 15.391C102.28 14.901 101.706 14.257 101.272 13.459C100.852 12.6469 100.642 11.7439 100.642 10.75C100.642 9.74195 100.859 8.83895 101.293 8.04095C101.727 7.22895 102.315 6.58495 103.057 6.10895C103.813 5.63295 104.646 5.39495 105.556 5.39495C106.158 5.39495 106.718 5.51395 107.236 5.75195C107.768 5.97595 108.23 6.31195 108.622 6.75995V0.94295L110.995 0.522949V16H108.643V14.6139C108.265 15.0899 107.796 15.461 107.236 15.727C106.676 15.979 106.06 16.1049 105.388 16.1049ZM106.123 14.11C106.627 14.11 107.096 14.012 107.53 13.816C107.964 13.606 108.328 13.319 108.622 12.955V8.52395C108.314 8.15995 107.943 7.87995 107.509 7.68395C107.075 7.48795 106.613 7.38995 106.123 7.38995C105.521 7.38995 104.982 7.53695 104.506 7.83095C104.044 8.11095 103.673 8.50295 103.393 9.00695C103.113 9.51095 102.973 10.092 102.973 10.75C102.973 11.38 103.113 11.9539 103.393 12.4719C103.673 12.976 104.044 13.375 104.506 13.669C104.982 13.9629 105.521 14.11 106.123 14.11Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M118.848 16V1.29995H121.368V7.47395H128.676V1.29995H131.196V16H128.676V9.72095H121.368V16H118.848Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M137.314 16.189C136.586 16.189 135.935 16.056 135.361 15.79C134.801 15.51 134.36 15.132 134.038 14.656C133.73 14.166 133.576 13.606 133.576 12.976C133.576 12.346 133.737 11.7999 134.059 11.3379C134.395 10.8759 134.864 10.519 135.466 10.267C136.068 10.015 136.782 9.88895 137.608 9.88895C138.098 9.88895 138.581 9.94495 139.057 10.0569C139.533 10.1549 139.995 10.323 140.443 10.561V9.38495C140.443 8.68495 140.24 8.15995 139.834 7.80995C139.442 7.45995 138.84 7.28495 138.028 7.28495C137.594 7.28495 137.125 7.35495 136.621 7.49495C136.131 7.62095 135.578 7.82395 134.962 8.10395L134.122 6.38195C135.662 5.66795 137.118 5.31095 138.49 5.31095C139.862 5.31095 140.919 5.64695 141.661 6.31895C142.417 6.97695 142.795 7.91495 142.795 9.13295V16H140.443V14.908C139.995 15.342 139.512 15.6639 138.994 15.874C138.476 16.084 137.916 16.189 137.314 16.189ZM135.802 12.934C135.802 13.424 135.998 13.809 136.39 14.089C136.782 14.3689 137.307 14.509 137.965 14.509C138.441 14.509 138.882 14.439 139.288 14.299C139.708 14.1449 140.093 13.9209 140.443 13.627V11.926C140.079 11.7579 139.701 11.6319 139.309 11.5479C138.917 11.464 138.49 11.422 138.028 11.422C137.342 11.422 136.796 11.5549 136.39 11.8209C135.998 12.0869 135.802 12.458 135.802 12.934Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M149.897 16.21C148.833 16.21 148.028 15.9649 147.482 15.4749C146.936 14.971 146.663 14.236 146.663 13.2699V7.36895H144.563V5.47895H146.663V2.58095L149.036 2.07695V5.47895H151.955V7.36895H149.036V12.745C149.036 13.2629 149.148 13.634 149.372 13.858C149.596 14.068 149.974 14.1729 150.506 14.1729C150.744 14.1729 150.961 14.1589 151.157 14.1309C151.367 14.089 151.626 14.0189 151.934 13.9209V15.9159C151.64 16.0139 151.304 16.084 150.926 16.1259C150.562 16.1819 150.219 16.21 149.897 16.21Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M73.916 38L79.964 23.2999H83.471L89.456 38H86.159L84.668 34.1359H78.599L77.087 38H73.916ZM79.544 31.6999H83.744L81.644 26.2819L79.544 31.6999Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M94.4493 38.2099C93.6093 38.2099 92.8603 38.028 92.2023 37.664C91.5583 37.286 91.0473 36.768 90.6693 36.11C90.3053 35.452 90.1233 34.6959 90.1233 33.8419V27.059H93.0003V33.422C93.0003 34.122 93.2033 34.682 93.6093 35.102C94.0293 35.522 94.5823 35.7319 95.2683 35.7319C96.2483 35.7319 97.0043 35.368 97.5363 34.6399V27.059H100.413V38H97.5363V37.118C96.6963 37.846 95.6673 38.2099 94.4493 38.2099Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M107.842 38.1679C106.625 38.1679 105.7 37.895 105.07 37.3489C104.454 36.7889 104.146 35.9769 104.146 34.9129V29.4529H101.899V27.059H104.146V24.2659L107.024 23.6149V27.059H110.153V29.4529H107.024V34.325C107.024 34.829 107.136 35.193 107.36 35.417C107.583 35.6269 107.975 35.7319 108.535 35.7319C108.815 35.7319 109.068 35.7179 109.292 35.6899C109.529 35.6479 109.789 35.5779 110.069 35.4799V37.853C109.775 37.951 109.404 38.028 108.956 38.084C108.522 38.1399 108.15 38.1679 107.842 38.1679Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M116.767 38.2099C115.675 38.2099 114.688 37.958 113.806 37.4539C112.924 36.9499 112.224 36.271 111.706 35.417C111.188 34.563 110.929 33.604 110.929 32.54C110.929 31.476 111.188 30.517 111.706 29.663C112.224 28.795 112.924 28.1089 113.806 27.6049C114.688 27.101 115.675 26.8489 116.767 26.8489C117.859 26.8489 118.846 27.101 119.728 27.6049C120.61 28.1089 121.31 28.795 121.828 29.663C122.346 30.517 122.605 31.476 122.605 32.54C122.605 33.604 122.346 34.563 121.828 35.417C121.31 36.271 120.61 36.9499 119.728 37.4539C118.846 37.958 117.859 38.2099 116.767 38.2099ZM116.767 35.7109C117.341 35.7109 117.852 35.5709 118.3 35.291C118.762 35.011 119.126 34.6329 119.392 34.1569C119.672 33.6669 119.812 33.128 119.812 32.54C119.812 31.938 119.672 31.399 119.392 30.923C119.126 30.447 118.762 30.069 118.3 29.7889C117.852 29.4949 117.341 29.3479 116.767 29.3479C116.207 29.3479 115.696 29.4949 115.234 29.7889C114.772 30.069 114.408 30.447 114.142 30.923C113.876 31.399 113.743 31.938 113.743 32.54C113.743 33.128 113.876 33.6669 114.142 34.1569C114.408 34.6329 114.772 35.011 115.234 35.291C115.696 35.5709 116.207 35.7109 116.767 35.7109Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M124.373 38V27.059H127.25V27.8989C128.034 27.1989 128.986 26.8489 130.106 26.8489C130.82 26.8489 131.457 26.996 132.017 27.2899C132.577 27.57 133.039 27.969 133.403 28.4869C134.313 27.3949 135.517 26.8489 137.015 26.8489C137.841 26.8489 138.562 27.038 139.178 27.416C139.808 27.78 140.298 28.291 140.648 28.9489C141.012 29.5929 141.194 30.3489 141.194 31.2169V38H138.338V31.6369C138.338 30.9229 138.149 30.3629 137.771 29.9569C137.393 29.5369 136.889 29.327 136.259 29.327C135.377 29.327 134.677 29.6909 134.159 30.4189C134.173 30.5449 134.187 30.6709 134.201 30.7969C134.215 30.9229 134.222 31.063 134.222 31.2169V38H131.345V31.6369C131.345 30.9229 131.156 30.3629 130.778 29.9569C130.414 29.5369 129.917 29.327 129.287 29.327C128.405 29.327 127.726 29.6629 127.25 30.3349V38H124.373Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M146.87 38.1889C146.086 38.1889 145.393 38.049 144.791 37.769C144.189 37.475 143.72 37.076 143.384 36.5719C143.048 36.0679 142.88 35.4869 142.88 34.8289C142.88 33.7789 143.272 32.9669 144.056 32.393C144.854 31.805 145.946 31.511 147.332 31.511C148.284 31.511 149.18 31.6579 150.02 31.952V31.1539C150.02 29.8799 149.25 29.243 147.71 29.243C147.248 29.243 146.751 29.32 146.219 29.4739C145.687 29.6139 145.071 29.8379 144.371 30.146L143.321 28.025C144.189 27.6329 145.015 27.3389 145.799 27.143C146.597 26.947 147.395 26.8489 148.193 26.8489C149.663 26.8489 150.804 27.2059 151.616 27.92C152.442 28.62 152.855 29.6139 152.855 30.9019V38H150.02V37.2229C149.572 37.5589 149.089 37.804 148.571 37.958C148.053 38.1119 147.486 38.1889 146.87 38.1889ZM145.61 34.7659C145.61 35.186 145.792 35.5219 146.156 35.7739C146.52 36.0119 147.003 36.131 147.605 36.131C148.571 36.131 149.376 35.893 150.02 35.417V33.8209C149.32 33.541 148.55 33.401 147.71 33.401C147.052 33.401 146.534 33.527 146.156 33.7789C145.792 34.0169 145.61 34.346 145.61 34.7659Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M159.912 38.1679C158.694 38.1679 157.77 37.895 157.14 37.3489C156.524 36.7889 156.216 35.9769 156.216 34.9129V29.4529H153.969V27.059H156.216V24.2659L159.093 23.6149V27.059H162.222V29.4529H159.093V34.325C159.093 34.829 159.205 35.193 159.429 35.417C159.653 35.6269 160.045 35.7319 160.605 35.7319C160.885 35.7319 161.137 35.7179 161.361 35.6899C161.599 35.6479 161.858 35.5779 162.138 35.4799V37.853C161.844 37.951 161.473 38.028 161.025 38.084C160.591 38.1399 160.22 38.1679 159.912 38.1679Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M163.625 38V27.059H166.502V38H163.625ZM165.053 25.757C164.605 25.757 164.22 25.596 163.898 25.274C163.576 24.952 163.415 24.5669 163.415 24.1189C163.415 23.6569 163.576 23.2719 163.898 22.9639C164.22 22.6419 164.605 22.4809 165.053 22.4809C165.515 22.4809 165.9 22.6419 166.208 22.9639C166.53 23.2719 166.691 23.6569 166.691 24.1189C166.691 24.5669 166.53 24.952 166.208 25.274C165.9 25.596 165.515 25.757 165.053 25.757Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M174.086 38.2099C172.994 38.2099 172.007 37.958 171.125 37.4539C170.243 36.9499 169.543 36.271 169.025 35.417C168.507 34.563 168.248 33.604 168.248 32.54C168.248 31.476 168.507 30.517 169.025 29.663C169.543 28.795 170.243 28.1089 171.125 27.6049C172.007 27.101 172.994 26.8489 174.086 26.8489C175.178 26.8489 176.165 27.101 177.047 27.6049C177.929 28.1089 178.629 28.795 179.147 29.663C179.665 30.517 179.924 31.476 179.924 32.54C179.924 33.604 179.665 34.563 179.147 35.417C178.629 36.271 177.929 36.9499 177.047 37.4539C176.165 37.958 175.178 38.2099 174.086 38.2099ZM174.086 35.7109C174.66 35.7109 175.171 35.5709 175.619 35.291C176.081 35.011 176.445 34.6329 176.711 34.1569C176.991 33.6669 177.131 33.128 177.131 32.54C177.131 31.938 176.991 31.399 176.711 30.923C176.445 30.447 176.081 30.069 175.619 29.7889C175.171 29.4949 174.66 29.3479 174.086 29.3479C173.526 29.3479 173.015 29.4949 172.553 29.7889C172.091 30.069 171.727 30.447 171.461 30.923C171.195 31.399 171.062 31.938 171.062 32.54C171.062 33.128 171.195 33.6669 171.461 34.1569C171.727 34.6329 172.091 35.011 172.553 35.291C173.015 35.5709 173.526 35.7109 174.086 35.7109Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M181.693 38V27.059H184.57V27.962C185.396 27.2199 186.418 26.8489 187.636 26.8489C188.49 26.8489 189.239 27.038 189.883 27.416C190.541 27.78 191.052 28.291 191.416 28.9489C191.78 29.5929 191.962 30.3489 191.962 31.2169V38H189.085V31.6369C189.085 30.9229 188.882 30.3629 188.476 29.9569C188.07 29.5369 187.517 29.327 186.817 29.327C186.327 29.327 185.893 29.425 185.515 29.621C185.137 29.803 184.822 30.0689 184.57 30.4189V38H181.693Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <line
            x1="66.5"
            y1="1.5"
            x2="66.5"
            y2="38.5"
            stroke="var(--pf-t--global--text--color--regular)"
            stroke-linecap="round"
          />
        </svg>
      </div>
      <div class="pf-v6-c-compass__nav">
        <div class="pf-v6-c-panel pf-m-pill pf-m-glass">
          <div class="pf-v6-c-panel__main">
            <div class="pf-v6-c-panel__main-body">
              <div class="pf-v6-c-compass__nav-content">
                <div class="pf-v6-c-compass__nav-home">
                  <button
                    class="pf-v6-c-button pf-m-circle pf-m-plain"
                    type="button"
                    aria-label="Home"
                  >
                    <span class="pf-v6-c-button__icon">
                      <svg
                        class="pf-v6-svg"
                        viewBox="0 0 32 32"
                        fill="currentColor"
                        aria-hidden="true"
                        role="img"
                        width="1em"
                        height="1em"
                      >
                        <path
                          d="M30.707 15.435 17.061 1.789a1.501 1.501 0 0 0-2.121 0L1.293 15.435a.999.999 0 1 0 1.414 1.414L3 16.556V29.5c0 .827.673 1.5 1.5 1.5h23c.827 0 1.5-.673 1.5-1.5V16.556l.293.293a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414ZM19 29h-6V19h6v10Zm8-10v10h-6V18.5c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5V29H5V14.556l11-11 11 11V19Z"
                        />
                      </svg>
                    </span>
                  </button>
                </div>
                <div class="pf-v6-c-compass__nav-main">
                  <nav
                    class="pf-v6-c-tabs pf-m-nav"
                    aria-label="Compass primary"
                  >
                    <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
                      <button
                        class="pf-v6-c-button pf-m-small pf-m-plain"
                        type="button"
                        aria-label="Scroll left"
                        disabled
                      >
                        <span class="pf-v6-c-button__icon">
                          <svg
                            class="pf-v6-svg"
                            viewBox="0 0 20 20"
                            fill="currentColor"
                            aria-hidden="true"
                            role="img"
                            width="1em"
                            height="1em"
                          >
                            <path
                              d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                            />
                          </svg>
                        </span>
                      </button>
                    </div>
                    <ul
                      class="pf-v6-c-tabs__list"
                      role="tablist"
                      aria-label="Compass primary"
                    >
                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="primary-nav-users-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Users</span>
                        </a>
                      </li>
                      <li
                        class="pf-v6-c-tabs__item pf-m-current"
                        role="presentation"
                      >
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="true"
                          id="primary-nav-containers-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Containers</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="primary-nav-database-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Database</span>
                        </a>
                      </li>

                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="primary-nav-server-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Server</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="primary-nav-system-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">System</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="primary-nav-network-wired-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Network</span>
                        </a>
                      </li>
                    </ul>

                    <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
                      <button
                        class="pf-v6-c-button pf-m-small pf-m-plain"
                        type="button"
                        aria-label="Scroll right"
                        disabled
                      >
                        <span class="pf-v6-c-button__icon">
                          <svg
                            class="pf-v6-svg"
                            viewBox="0 0 20 20"
                            fill="currentColor"
                            aria-hidden="true"
                            role="img"
                            width="1em"
                            height="1em"
                          >
                            <path
                              d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                            />
                          </svg>
                        </span>
                      </button>
                    </div>
                  </nav>
                </div>
                <div class="pf-v6-c-compass__nav-search">
                  <button
                    class="pf-v6-c-button pf-m-circle pf-m-plain"
                    type="button"
                    aria-label="Search"
                  >
                    <span class="pf-v6-c-button__icon">
                      <svg
                        class="pf-v6-svg"
                        viewBox="0 0 32 32"
                        fill="currentColor"
                        aria-hidden="true"
                        role="img"
                        width="1em"
                        height="1em"
                      >
                        <path
                          d="m30.796 29.205-8.557-8.557A11.945 11.945 0 0 0 25 13c0-6.617-5.383-12-12-12S1 6.383 1 13s5.383 12 12 12c2.904 0 5.57-1.038 7.648-2.761l8.556 8.556a1.122 1.122 0 0 0 1.592 0 1.127 1.127 0 0 0 0-1.591ZM3 13C3 7.486 7.486 3 13 3s10 4.486 10 10-4.486 10-10 10S3 18.514 3 13Z"
                        />
                      </svg>
                    </span>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="pf-v6-c-panel pf-m-pill pf-m-glass">
          <div class="pf-v6-c-panel__main">
            <div class="pf-v6-c-panel__main-body">
              <div class="pf-v6-c-compass__nav-content">
                <div class="pf-v6-c-compass__nav-main">
                  <nav
                    class="pf-v6-c-tabs pf-m-nav pf-m-subtab"
                    aria-label="Compass secondary"
                  >
                    <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
                      <button
                        class="pf-v6-c-button pf-m-small pf-m-plain"
                        type="button"
                        aria-label="Scroll left"
                        disabled
                      >
                        <span class="pf-v6-c-button__icon">
                          <svg
                            class="pf-v6-svg"
                            viewBox="0 0 20 20"
                            fill="currentColor"
                            aria-hidden="true"
                            role="img"
                            width="1em"
                            height="1em"
                          >
                            <path
                              d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                            />
                          </svg>
                        </span>
                      </button>
                    </div>
                    <ul
                      class="pf-v6-c-tabs__list"
                      role="tablist"
                      aria-label="Compass secondary"
                    >
                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="secondary-nav-sub-1-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Item 1</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="secondary-nav-sub-2-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Item 2</span>
                        </a>
                      </li>
                      <li
                        class="pf-v6-c-tabs__item pf-m-current"
                        role="presentation"
                      >
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="true"
                          id="secondary-nav-sub-3-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Item 3</span>
                        </a>
                      </li>

                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link pf-m-disabled"
                          aria-disabled="true"
                          tabindex="-1"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="secondary-nav-sub-disabled-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Disabled</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link pf-m-aria-disabled"
                          aria-disabled="true"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="secondary-nav-sub-aria-disabled-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="secondary-nav-sub-6-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Item 6</span>
                        </a>
                      </li>
                    </ul>

                    <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
                      <button
                        class="pf-v6-c-button pf-m-small pf-m-plain"
                        type="button"
                        aria-label="Scroll right"
                        disabled
                      >
                        <span class="pf-v6-c-button__icon">
                          <svg
                            class="pf-v6-svg"
                            viewBox="0 0 20 20"
                            fill="currentColor"
                            aria-hidden="true"
                            role="img"
                            width="1em"
                            height="1em"
                          >
                            <path
                              d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                            />
                          </svg>
                        </span>
                      </button>
                    </div>
                  </nav>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-compass__profile">
        <button
          class="pf-v6-c-menu-toggle pf-m-circle pf-m-text pf-m-plain"
          type="button"
          aria-expanded="false"
        >
          <span class="pf-v6-c-menu-toggle__icon">
            <img
              class="pf-v6-c-avatar pf-m-md"
              alt="Avatar image"
              src="/assets/images/img_avatar-light.svg"
            />
          </span>
          <span class="pf-v6-c-menu-toggle__text">Ned Username</span>
          <span class="pf-v6-c-menu-toggle__controls">
            <span class="pf-v6-c-menu-toggle__toggle-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </div>
    </div>
    <div class="pf-v6-c-compass__sidebar pf-m-expanded pf-m-start">
      <div class="pf-v6-c-panel pf-m-pill pf-m-glass">
        <div class="pf-v6-c-panel__main">
          <div class="pf-v6-c-panel__main-body">
            <div class="pf-v6-c-action-list pf-m-icons pf-m-vertical">
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="Add"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M28.5 2h-25C2.673 2 2 2.673 2 3.5v25c0 .827.673 1.5 1.5 1.5h25c.827 0 1.5-.673 1.5-1.5v-25c0-.827-.673-1.5-1.5-1.5ZM28 28H4V4h24v24ZM8 16a1 1 0 0 1 1-1h6V9a1 1 0 1 1 2 0v6h6a1 1 0 1 1 0 2h-6v6a1 1 0 1 1-2 0v-6H9a1 1 0 0 1-1-1Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="Collections"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M28.5 11h-25c-.827 0-1.5.673-1.5 1.5v17c0 .827.673 1.5 1.5 1.5h25c.827 0 1.5-.673 1.5-1.5v-17c0-.827-.673-1.5-1.5-1.5ZM28 29H4V13h24v16ZM6 2a1 1 0 0 1 1-1h18a1 1 0 0 1 0 2H7a1 1 0 0 1-1-1ZM4 7a1 1 0 0 1 1-1h22a1 1 0 0 1 0 2H5a1 1 0 0 1-1-1Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-v6-m-ai-indicator pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="AI assistant"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M30.502 7c0 .29-.209.536-.498.59a5.523 5.523 0 0 0-4.417 4.417c-.054.289-.3.498-.59.498s-.536-.21-.59-.498A5.52 5.52 0 0 0 19.99 7.59c-.289-.054-.498-.3-.498-.59s.21-.536.498-.59a5.52 5.52 0 0 0 4.417-4.417c.054-.289.301-.498.59-.498s.536.21.59.498a5.523 5.523 0 0 0 4.417 4.417c.289.054.498.3.498.59Zm-4.465 9.962A11.932 11.932 0 0 1 15.038 5.97C15.001 5.447 14.524 5 14 5c-.521 0-.997.442-1.038.962a11.932 11.932 0 0 1-10.992 11C1.447 16.999 1 17.476 1 18c0 .521.442.997.962 1.038a11.932 11.932 0 0 1 11 10.992c.037.524.514.97 1.038.97.521 0 .997-.442 1.038-.962a11.933 11.933 0 0 1 11-10.999c.519-.042.961-.516.961-1.038 0-.521-.442-.997-.962-1.038Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="Volume"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M17.439 2.102a1 1 0 0 0-1.054.109L7.656 9H2.5C1.673 9 1 9.673 1 10.5v11c0 .827.673 1.5 1.5 1.5h5.157l8.729 6.789a.998.998 0 0 0 1.053.109c.343-.168.561-.517.561-.898V3a1 1 0 0 0-.561-.898ZM16 26.955l-7.386-5.744A1 1 0 0 0 8 21H3V11h5a.997.997 0 0 0 .614-.211L16 5.045v21.91ZM31 16a14.94 14.94 0 0 1-4.284 10.488.997.997 0 0 1-1.414.018 1 1 0 0 1-.018-1.414C27.68 22.637 29 19.408 29 16s-1.319-6.637-3.716-9.092a.999.999 0 1 1 1.432-1.396A14.94 14.94 0 0 1 31 16Zm-6 0a9.007 9.007 0 0 1-2.249 5.95.996.996 0 0 1-1.411.091 1 1 0 0 1-.091-1.411C22.378 19.346 23 17.702 23 16s-.622-3.346-1.751-4.63a1 1 0 0 1 1.502-1.32A9.007 9.007 0 0 1 25 16Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="Use microphone"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M16 22c3.86 0 7-3.141 7-7V8c0-3.859-3.14-7-7-7S9 4.141 9 8v7c0 3.859 3.14 7 7 7ZM11 8c0-2.757 2.243-5 5-5s5 2.243 5 5v7c0 2.757-2.243 5-5 5s-5-2.243-5-5V8Zm5.99 17.95c0 .018.01.032.01.05v2.021h5a1 1 0 1 1 0 2H10.02a1 1 0 1 1 0-2H15V26c0-.018.009-.033.01-.05C9.407 25.447 5 20.731 5 15a1 1 0 1 1 2 0c0 4.963 4.038 9 9 9s9-4.037 9-9a1 1 0 1 1 2 0c0 5.731-4.407 10.447-10.01 10.95Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="pf-v6-c-compass__main">
      <div class="pf-v6-c-compass__hero">
        <div
          class="pf-v6-c-hero pf-m-glass"
          style="
                  --pf-v6-c-hero--gradient--stop-1--dark: #3d2785;
                  --pf-v6-c-hero--gradient--stop-2--dark: #1b0d33;
                  --pf-v6-c-hero--gradient--stop-3--dark: #000;
                  --pf-v6-c-hero--BackgroundImage--light: url(/assets/images/compass--hero-bg.png);
                  --pf-v6-c-hero--BackgroundImage--dark: url(/assets/images/compass--hero-bg.png);
                "
        >
          <div class="pf-v6-c-hero__body">
            <div class="pf-v6-c-content">
              <h1>Automation that does more</h1>
              <p>Red&nbsp;Hat Ansible Automation Platform offers more capabilities, accessibility, and flexibility, so you can bring the power of automation to the teams, tasks, and environments that need it.</p>
              <div class="pf-v6-c-action-list">
                <div class="pf-v6-c-action-list__group">
                  <div class="pf-v6-c-action-list__item">
                    <button class="pf-v6-c-button pf-m-primary" type="button">
                      <span class="pf-v6-c-button__text">Upgrade today</span>
                    </button>
                  </div>
                  <div class="pf-v6-c-action-list__item">
                    <button class="pf-v6-c-button pf-m-secondary" type="button">
                      <span class="pf-v6-c-button__text">Talk to a Red Hatter</span>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-compass__content">
        <div class="pf-v6-l-grid pf-m-gutter">
          <div
            class="pf-v6-l-grid__item pf-m-gutter pf-m-4-col-on-lg pf-m-6-col-on-2xl"
            style="--pf-v6-l-grid--item--Order-on-lg:3"
          >
            <div class="pf-v6-l-flex pf-m-column">
              <div
                class="pf-v6-c-card pf-m-glass"
                id="compass-dashboard-grid-status-card-1"
              >
                <div class="pf-v6-c-card__header">
                  <h2 class="pf-v6-c-title pf-m-xl">Status</h2>
                </div>
                <div class="pf-v6-c-card__body">
                  <div
                    class="pf-v6-l-gallery pf-m-gutter"
                    style="--pf-v6-l-gallery--GridTemplateColumns--min: 100%; --pf-v6-l-gallery--GridTemplateColumns--min-on-sm: 180px; --pf-v6-l-gallery--GridTemplateColumns--min-on-lg: 150px; --pf-v6-l-gallery--GridTemplateColumns--max-on-sm: 1fr;"
                  >
                    <div class="pf-v6-l-flex pf-m-space-items-sm pf-m-nowrap">
                      <div class="pf-v6-l-flex__item">
                        <span class="pf-v6-c-icon">
                          <span class="pf-v6-c-icon__content pf-m-success">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                              />
                            </svg>
                          </span>
                        </span>
                      </div>
                      <div class="pf-v6-l-flex__item">
                        <span>Cluster</span>
                      </div>
                    </div>
                    <div class="pf-v6-l-flex pf-m-space-items-sm pf-m-nowrap">
                      <div class="pf-v6-l-flex__item">
                        <span class="pf-v6-c-icon">
                          <span class="pf-v6-c-icon__content pf-m-danger">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm-1.5 8a1.5 1.5 0 1 1 3 0v7a1.5 1.5 0 1 1-3 0V9ZM16 25.001a2 2 0 1 1-.001-3.999A2 2 0 0 1 16 25.001Z"
                              />
                            </svg>
                          </span>
                        </span>
                      </div>
                      <div class="pf-v6-l-flex__item pf-v6-u-text-nowrap">
                        <span class="popover-parent">
                          <a href="#">Control Panel</a>
                        </span>
                      </div>
                    </div>
                    <div class="pf-v6-l-flex pf-m-space-items-sm pf-m-nowrap">
                      <div class="pf-v6-l-flex__item pf-v6-u-text-nowrap">
                        <span class="pf-v6-c-icon">
                          <span class="pf-v6-c-icon__content pf-m-danger">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm-1.5 8a1.5 1.5 0 1 1 3 0v7a1.5 1.5 0 1 1-3 0V9ZM16 25.001a2 2 0 1 1-.001-3.999A2 2 0 0 1 16 25.001Z"
                              />
                            </svg>
                          </span>
                        </span>
                      </div>
                      <div
                        class="pf-v6-l-flex pf-m-column pf-m-space-items-none"
                      >
                        <div class="pf-v6-l-flex__item">
                          <a href="#">Operators</a>
                        </div>
                        <div class="pf-v6-l-flex__item">
                          <span class="pf-v6-u-text-color-subtle">1 degraded</span>
                        </div>
                      </div>
                    </div>
                    <div class="pf-v6-l-flex pf-m-space-items-sm pf-m-nowrap">
                      <div class="pf-v6-l-flex__item">
                        <span class="pf-v6-c-icon">
                          <span class="pf-v6-c-icon__content pf-m-success">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                              />
                            </svg>
                          </span>
                        </span>
                      </div>
                      <div
                        class="pf-v6-l-flex pf-m-column pf-m-space-items-none"
                      >
                        <div class="pf-v6-l-flex__item">
                          <a href="#">Image Vulnerabilities</a>
                        </div>
                        <div class="pf-v6-l-flex__item">
                          <span class="pf-v6-u-color-200">0 vulnerabilities</span>
                        </div>
                      </div>
                    </div>
                    <div class="pf-v6-l-flex pf-m-space-items-sm pf-m-nowrap">
                      <div class="pf-v6-l-flex__item">
                        <span class="pf-v6-c-icon">
                          <span class="pf-v6-c-icon__content pf-m-success">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                              />
                            </svg>
                          </span>
                        </span>
                      </div>
                      <div
                        class="pf-v6-l-flex pf-m-column pf-m-space-items-none"
                      >
                        <div class="pf-v6-l-flex__item">
                          <a href="#">Storage</a>
                        </div>
                        <div class="pf-v6-l-flex__item">
                          <span class="pf-v6-u-color-200">Degraded</span>
                        </div>
                      </div>
                    </div>
                    <div class="pf-v6-l-flex pf-m-space-items-sm pf-m-nowrap">
                      <div class="pf-v6-l-flex__item">
                        <span class="pf-v6-c-icon">
                          <span class="pf-v6-c-icon__content pf-m-success">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                              />
                            </svg>
                          </span>
                        </span>
                      </div>
                      <div
                        class="pf-v6-l-flex pf-m-column pf-m-space-items-none"
                      >
                        <div class="pf-v6-l-flex__item">
                          <a href="#">Hardware</a>
                        </div>
                      </div>
                    </div>
                    <div class="pf-v6-l-flex pf-m-space-items-sm pf-m-nowrap">
                      <div class="pf-v6-l-flex__item">
                        <span class="pf-v6-c-icon">
                          <span class="pf-v6-c-icon__content pf-m-success">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                              />
                            </svg>
                          </span>
                        </span>
                      </div>
                      <div
                        class="pf-v6-l-flex pf-m-column pf-m-space-items-none"
                      >
                        <div class="pf-v6-l-flex__item">
                          <a href="#">Insights</a>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="pf-v6-c-card pf-m-glass"
                id="compass-dashboard-grid-line-chart-card-1"
              >
                <div class="pf-v6-c-card__header">
                  <div class="pf-v6-c-card__actions pf-m-no-offset">
                    <button
                      class="pf-v6-c-menu-toggle pf-m-text pf-m-plain"
                      type="button"
                      aria-expanded="false"
                      id="compass-dashboard-grid-line-chart-card-1-select-dropdown"
                    >
                      <span class="pf-v6-c-menu-toggle__text">24 hours</span>
                      <span class="pf-v6-c-menu-toggle__controls">
                        <span class="pf-v6-c-menu-toggle__toggle-icon">
                          <svg
                            class="pf-v6-svg"
                            viewBox="0 0 20 20"
                            fill="currentColor"
                            aria-hidden="true"
                            role="img"
                            width="1em"
                            height="1em"
                          >
                            <path
                              d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
                            />
                          </svg>
                        </span>
                      </span>
                    </button>
                  </div>
                  <div
                    class="pf-v6-c-card__title"
                    id="compass-dashboard-grid-line-chart-card-1-title"
                  >
                    <h2 class="pf-v6-c-title pf-m-xl">Cluster utilizations</h2>
                  </div>
                </div>
                <div
                  class="pf-v6-c-card pf-m-plain pf-m-expanded"
                  id="compass-dashboard-grid-line-chart-card-1-group-1"
                >
                  <div class="pf-v6-c-card__header pf-m-toggle-right">
                    <div class="pf-v6-c-card__header-toggle">
                      <button
                        class="pf-v6-c-button pf-m-plain"
                        id="compass-dashboard-grid-line-chart-card-1-group-1-toggle"
                        type="button"
                        aria-labelledby="compass-dashboard-grid-line-chart-card-1-group-1-title compass-dashboard-grid-line-chart-card-1-group-1-toggle"
                        aria-label="Details"
                      >
                        <span class="pf-v6-c-button__icon pf-m-start">
                          <span class="pf-v6-c-card__header-toggle-icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 20 20"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M18.71 5.29a.996.996 0 0 0-1.41 0l-7.29 7.29-7.3-7.29a.987.987 0 0 0-1.41-.02.987.987 0 0 0-.02 1.41l.02.02 7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65a.996.996 0 0 0 0-1.41Z"
                              />
                            </svg>
                          </span>
                        </span>
                      </button>
                    </div>
                    <div class="pf-v6-c-card__title">
                      <h2
                        class="pf-v6-c-card__title-text"
                        id="compass-dashboard-grid-line-chart-card-1-group-1-title"
                      >CPU 1</h2>
                    </div>
                  </div>
                  <div class="pf-v6-c-card__expandable-content">
                    <div class="pf-v6-c-card__body">
                      <div class="pf-v6-l-grid pf-m-gutter">
                        <div class="pf-v6-l-grid pf-m-gutter">
                          <div class="pf-v6-l-grid__item pf-m-4-col-on-md">
                            <div
                              class="pf-v6-l-flex pf-m-column-on-md pf-m-space-items-none-on-md pf-m-justify-content-center-on-md pf-v6-u-h-100-on-md"
                            >
                              <div class="pf-v6-l-flex__item">
                                <b>Temperature</b>
                              </div>
                              <hr
                                class="pf-v6-c-divider pf-m-vertical pf-m-inset-sm pf-v6-u-hidden-on-md"
                              />
                              <div class="pf-v6-l-flex__item">
                                <span>64C</span>
                              </div>
                            </div>
                          </div>
                          <div class="pf-v6-l-grid__item pf-m-8-col-on-md">
                            <div class="pf-v6-l-grid pf-m-gutter">
                              <div class="pf-v6-l-grid__item pf-m-2-col">
                                <div
                                  class="pf-v6-l-flex pf-m-column pf-m-space-items-none pf-m-align-items-flex-end-on-md"
                                >
                                  <div class="pf-v6-l-flex__item">100C</div>
                                  <div class="pf-v6-l-flex__item">50C</div>
                                  <div class="pf-v6-l-flex__item">0C</div>
                                </div>
                              </div>
                              <div class="pf-v6-l-grid__item pf-m-10-col">
                                <div class="ws-chart">
                                  <img
                                    src="/assets/images/img_line-chart-2.png"
                                    alt="Line chart"
                                  />
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                        <hr class="pf-v6-c-divider pf-v6-u-hidden-on-md" />
                        <div class="pf-v6-l-grid pf-m-gutter">
                          <div class="pf-v6-l-grid__item pf-m-4-col-on-md">
                            <div
                              class="pf-v6-l-flex pf-m-column-on-md pf-m-space-items-none-on-md pf-m-justify-content-center-on-md pf-v6-u-h-100-on-md"
                            >
                              <div class="pf-v6-l-flex__item">
                                <b>Speed</b>
                              </div>
                              <hr
                                class="pf-v6-c-divider pf-m-vertical pf-m-inset-sm pf-v6-u-hidden-on-md"
                              />
                              <div class="pf-v6-l-flex__item">
                                <span>2.3Ghz</span>
                              </div>
                            </div>
                          </div>
                          <div class="pf-v6-l-grid__item pf-m-8-col-on-md">
                            <div class="pf-v6-l-grid pf-m-gutter">
                              <div class="pf-v6-l-grid__item pf-m-2-col">
                                <div
                                  class="pf-v6-l-flex pf-m-column pf-m-space-items-none pf-m-align-items-flex-end-on-md"
                                >
                                  <div class="pf-v6-l-flex__item">36hz</div>
                                  <div class="pf-v6-l-flex__item">1.5Ghz</div>
                                  <div class="pf-v6-l-flex__item">0Ghz</div>
                                </div>
                              </div>
                              <div class="pf-v6-l-grid__item pf-m-10-col">
                                <div class="ws-chart">
                                  <img
                                    src="/assets/images/img_line-chart-2.png"
                                    alt="Line chart"
                                  />
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div
                  class="pf-v6-c-card pf-m-plain"
                  id="compass-dashboard-grid-line-chart-card-1-group-2"
                >
                  <div class="pf-v6-c-card__header pf-m-toggle-right">
                    <div class="pf-v6-c-card__header-toggle">
                      <button
                        class="pf-v6-c-button pf-m-plain"
                        id="compass-dashboard-grid-line-chart-card-1-group-2-toggle"
                        type="button"
                        aria-labelledby="compass-dashboard-grid-line-chart-card-1-group-2-title compass-dashboard-grid-line-chart-card-1-group-2-toggle"
                        aria-label="Details"
                      >
                        <span class="pf-v6-c-button__icon pf-m-start">
                          <span class="pf-v6-c-card__header-toggle-icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 20 20"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M18.71 5.29a.996.996 0 0 0-1.41 0l-7.29 7.29-7.3-7.29a.987.987 0 0 0-1.41-.02.987.987 0 0 0-.02 1.41l.02.02 7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65a.996.996 0 0 0 0-1.41Z"
                              />
                            </svg>
                          </span>
                        </span>
                      </button>
                    </div>
                    <div class="pf-v6-c-card__title">
                      <h2
                        class="pf-v6-c-card__title-text"
                        id="compass-dashboard-grid-line-chart-card-1-group-2-title"
                      >Pod count</h2>
                    </div>
                  </div>
                </div>
                <div
                  class="pf-v6-c-card pf-m-plain"
                  id="compass-dashboard-grid-line-chart-card-1-group-3"
                >
                  <div class="pf-v6-c-card__header pf-m-toggle-right">
                    <div class="pf-v6-c-card__header-toggle">
                      <button
                        class="pf-v6-c-button pf-m-plain"
                        id="compass-dashboard-grid-line-chart-card-1-group-3-toggle"
                        type="button"
                        aria-labelledby="compass-dashboard-grid-line-chart-card-1-group-3-title compass-dashboard-grid-line-chart-card-1-group-3-toggle"
                        aria-label="Details"
                      >
                        <span class="pf-v6-c-button__icon pf-m-start">
                          <span class="pf-v6-c-card__header-toggle-icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 20 20"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M18.71 5.29a.996.996 0 0 0-1.41 0l-7.29 7.29-7.3-7.29a.987.987 0 0 0-1.41-.02.987.987 0 0 0-.02 1.41l.02.02 7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65a.996.996 0 0 0 0-1.41Z"
                              />
                            </svg>
                          </span>
                        </span>
                      </button>
                    </div>
                    <div class="pf-v6-c-card__title">
                      <h2
                        class="pf-v6-c-card__title-text"
                        id="compass-dashboard-grid-line-chart-card-1-group-3-title"
                      >Memory</h2>
                    </div>
                  </div>
                </div>
              </div>
              <div class="pf-v6-c-card pf-m-glass">
                <div class="pf-v6-c-card__title">
                  <h2 class="pf-v6-c-title pf-m-xl">Recomendations by severity</h2>
                </div>
                <div class="pf-v6-c-card__body">
                  <div class="pf-v6-l-flex pf-m-inline-flex">
                    <div class="pf-v6-l-grid pf-m-gutter pf-m-all-3-col">
                      <div
                        class="pf-v6-l-flex pf-m-column pf-m-space-items-xs pf-m-align-items-center"
                      >
                        <span
                          class="pf-v6-u-font-size-2xl pf-v6-u-primary-color-100"
                        >2</span>
                        <span class="pf-v6-u-font-color-200">Critical</span>
                      </div>
                      <div
                        class="pf-v6-l-flex pf-m-column pf-m-space-items-xs pf-m-align-items-center"
                      >
                        <span
                          class="pf-v6-u-font-size-2xl pf-v6-u-primary-color-100"
                        >5</span>
                        <span class="pf-v6-u-font-color-200">Important</span>
                      </div>
                      <div
                        class="pf-v6-l-flex pf-m-column pf-m-space-items-xs pf-m-align-items-center"
                      >
                        <span
                          class="pf-v6-u-font-size-2xl pf-v6-u-primary-color-100"
                        >7</span>
                        <span class="pf-v6-u-font-color-200">Moderate</span>
                      </div>
                      <div
                        class="pf-v6-l-flex pf-m-column pf-m-space-items-xs pf-m-align-items-center"
                      >
                        <span
                          class="pf-v6-u-font-size-2xl pf-v6-u-primary-color-100"
                        >12</span>
                        <span class="pf-v6-u-font-color-200">Low</span>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="pf-v6-c-card__title">
                  <h2 class="pf-v6-c-title pf-m-xl">Recomendations by category</h2>
                </div>
                <div class="pf-v6-c-card__body">
                  <img
                    src="/assets/images/img_pie-chart-with-legend.png"
                    alt="Pie chart"
                    width="450"
                  />
                </div>
                <div class="pf-v6-c-card__footer">
                  <a href="#">View more</a>
                </div>
              </div>
            </div>
          </div>
          <div
            class="pf-v6-l-grid__item pf-m-gutter pf-m-4-col-on-lg pf-m-3-col-on-2xl"
            style="--pf-v6-l-grid--item--Order-on-lg:2"
          >
            <div
              class="pf-v6-l-flex pf-m-column pf-m-row-on-md pf-m-column-on-lg"
            >
              <div class="pf-v6-l-flex__item pf-m-flex-1">
                <div
                  class="pf-v6-c-card pf-m-glass"
                  id="compass-dashboard-grid-details-card-1"
                >
                  <div class="pf-v6-c-card__title">
                    <h2 class="pf-v6-c-title pf-m-xl">Details</h2>
                  </div>
                  <div class="pf-v6-c-card__body">
                    <dl class="pf-v6-c-description-list" aria-label="Details">
                      <div class="pf-v6-c-description-list__group">
                        <dt
                          class="pf-v6-c-description-list__term"
                        >Cluster API Address</dt>
                        <dd class="pf-v6-c-description-list__description">
                          <div class="pf-v6-c-description-list__text">
                            <a href="#">https://api1.devcluster.openshift.com</a>
                          </div>
                        </dd>
                      </div>
                      <div class="pf-v6-c-description-list__group">
                        <dt class="pf-v6-c-description-list__term">Cluster ID</dt>
                        <dd class="pf-v6-c-description-list__description">
                          <div
                            class="pf-v6-c-description-list__text"
                          >63b97ac1-b850-41d9-8820-239becde9e86</div>
                        </dd>
                      </div>
                      <div class="pf-v6-c-description-list__group">
                        <dt class="pf-v6-c-description-list__term">Provider</dt>
                        <dd class="pf-v6-c-description-list__description">
                          <div class="pf-v6-c-description-list__text">AWS</div>
                        </dd>
                      </div>
                      <div class="pf-v6-c-description-list__group">
                        <dt
                          class="pf-v6-c-description-list__term"
                        >OpenShift Version</dt>
                        <dd class="pf-v6-c-description-list__description">
                          <div
                            class="pf-v6-c-description-list__text"
                          >4.5.0.ci-2020-06-16-015028</div>
                        </dd>
                      </div>
                      <div class="pf-v6-c-description-list__group">
                        <dt
                          class="pf-v6-c-description-list__term"
                        >Update Channel</dt>
                        <dd class="pf-v6-c-description-list__description">
                          <div class="pf-v6-c-description-list__text">stable-4.5</div>
                        </dd>
                      </div>
                    </dl>
                  </div>
                  <hr class="pf-v6-c-divider" />
                  <div class="pf-v6-c-card__footer">
                    <a href="#">View Settings</a>
                  </div>
                </div>
              </div>
              <div class="pf-v6-l-flex__item pf-m-flex-1">
                <div
                  class="pf-v6-c-card pf-m-glass"
                  id="compass-dashboard-grid-data-list-card-1"
                >
                  <div
                    class="pf-v6-c-card__header pf-v6-u-align-items-flex-start"
                  >
                    <div
                      class="pf-v6-c-card__title"
                      id="compass-dashboard-grid-data-list-card-1-title1"
                    >
                      <h2 class="pf-v6-c-title pf-m-lg">Inventory</h2>
                    </div>
                  </div>
                  <ul
                    class="pf-v6-c-data-list pf-m-plain pf-m-grid-none"
                    role="list"
                    aria-label="Simple data list example"
                    id="compass-dashboard-grid-data-list-card-1-data-list"
                  >
                    <li class="pf-v6-c-data-list__item">
                      <div class="pf-v6-c-data-list__item-row">
                        <div class="pf-v6-c-data-list__item-content">
                          <div
                            class="pf-v6-c-data-list__cell"
                            id="compass-dashboard-grid-data-list-card-1-data-list-item-1"
                          >3 Nodes</div>
                          <div
                            class="pf-v6-c-data-list__cell pf-m-no-fill pf-m-align-right"
                          >
                            <a href="#">
                              <div class="pf-v6-l-flex pf-m-space-items-sm">
                                <span>3</span>
                                <span class="pf-v6-c-icon">
                                  <span
                                    class="pf-v6-c-icon__content pf-m-success"
                                  >
                                    <svg
                                      class="pf-v6-svg"
                                      viewBox="0 0 32 32"
                                      fill="currentColor"
                                      aria-hidden="true"
                                      role="img"
                                      width="1em"
                                      height="1em"
                                    >
                                      <path
                                        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                                      />
                                    </svg>
                                  </span>
                                </span>
                              </div>
                            </a>
                          </div>
                        </div>
                      </div>
                    </li>
                    <li class="pf-v6-c-data-list__item">
                      <div class="pf-v6-c-data-list__item-row">
                        <div class="pf-v6-c-data-list__item-content">
                          <div
                            class="pf-v6-c-data-list__cell"
                            id="compass-dashboard-grid-data-list-card-1-data-list-item-2"
                          >8 Disks</div>
                          <div
                            class="pf-v6-c-data-list__cell pf-m-no-fill pf-m-align-right"
                          >
                            <a href="#">
                              <div class="pf-v6-l-flex pf-m-space-items-sm">
                                <span>8</span>
                                <span class="pf-v6-c-icon">
                                  <span
                                    class="pf-v6-c-icon__content pf-m-success"
                                  >
                                    <svg
                                      class="pf-v6-svg"
                                      viewBox="0 0 32 32"
                                      fill="currentColor"
                                      aria-hidden="true"
                                      role="img"
                                      width="1em"
                                      height="1em"
                                    >
                                      <path
                                        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                                      />
                                    </svg>
                                  </span>
                                </span>
                              </div>
                            </a>
                          </div>
                        </div>
                      </div>
                    </li>
                    <li class="pf-v6-c-data-list__item">
                      <div class="pf-v6-c-data-list__item-row">
                        <div class="pf-v6-c-data-list__item-content">
                          <div
                            class="pf-v6-c-data-list__cell"
                            id="compass-dashboard-grid-data-list-card-1-data-list-item-3"
                          >20 Pods</div>
                          <div
                            class="pf-v6-c-data-list__cell pf-m-no-fill pf-m-align-right"
                          >
                            <a href="#">
                              <div class="pf-v6-l-flex pf-m-space-items-sm">
                                <span>20</span>
                                <span class="pf-v6-c-icon">
                                  <span
                                    class="pf-v6-c-icon__content pf-m-success"
                                  >
                                    <svg
                                      class="pf-v6-svg"
                                      viewBox="0 0 32 32"
                                      fill="currentColor"
                                      aria-hidden="true"
                                      role="img"
                                      width="1em"
                                      height="1em"
                                    >
                                      <path
                                        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                                      />
                                    </svg>
                                  </span>
                                </span>
                              </div>
                            </a>
                          </div>
                        </div>
                      </div>
                    </li>
                    <li class="pf-v6-c-data-list__item">
                      <div class="pf-v6-c-data-list__item-row">
                        <div class="pf-v6-c-data-list__item-content">
                          <div
                            class="pf-v6-c-data-list__cell"
                            id="compass-dashboard-grid-data-list-card-1-data-list-item-4"
                          >12 PVs</div>
                          <div
                            class="pf-v6-c-data-list__cell pf-m-no-fill pf-m-align-right"
                          >
                            <a href="#">
                              <div class="pf-v6-l-flex pf-m-space-items-sm">
                                <span>12</span>
                                <span class="pf-v6-c-icon">
                                  <span
                                    class="pf-v6-c-icon__content pf-m-success"
                                  >
                                    <svg
                                      class="pf-v6-svg"
                                      viewBox="0 0 32 32"
                                      fill="currentColor"
                                      aria-hidden="true"
                                      role="img"
                                      width="1em"
                                      height="1em"
                                    >
                                      <path
                                        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                                      />
                                    </svg>
                                  </span>
                                </span>
                              </div>
                            </a>
                          </div>
                        </div>
                      </div>
                    </li>
                    <li class="pf-v6-c-data-list__item">
                      <div class="pf-v6-c-data-list__item-row">
                        <div class="pf-v6-c-data-list__item-content">
                          <div
                            class="pf-v6-c-data-list__cell"
                            id="compass-dashboard-grid-data-list-card-1-data-list-item-5"
                          >18 PVCs</div>
                          <div
                            class="pf-v6-c-data-list__cell pf-m-no-fill pf-m-align-right"
                          >
                            <a href="#">
                              <div class="pf-v6-l-flex pf-m-space-items-sm">
                                <span>18</span>
                                <span class="pf-v6-c-icon">
                                  <span
                                    class="pf-v6-c-icon__content pf-m-success"
                                  >
                                    <svg
                                      class="pf-v6-svg"
                                      viewBox="0 0 32 32"
                                      fill="currentColor"
                                      aria-hidden="true"
                                      role="img"
                                      width="1em"
                                      height="1em"
                                    >
                                      <path
                                        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                                      />
                                    </svg>
                                  </span>
                                </span>
                              </div>
                            </a>
                          </div>
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          <div
            class="pf-v6-l-grid__item pf-m-4-col-on-lg pf-m-3-col-on-2xl"
            style="--pf-v6-l-grid--item--Order-on-lg:4"
          >
            <div class="pf-v6-l-flex pf-m-column">
              <div
                class="pf-v6-c-card pf-m-glass"
                id="compass-dashboard-grid-events-card-1"
              >
                <div class="pf-v6-c-card__header">
                  <div class="pf-v6-c-card__actions pf-m-no-offset">
                    <button
                      class="pf-v6-c-menu-toggle pf-m-text pf-m-plain"
                      type="button"
                      aria-expanded="false"
                      id="compass-dashboard-grid-events-card-1-select-dropdown"
                    >
                      <span class="pf-v6-c-menu-toggle__text">Status</span>
                      <span class="pf-v6-c-menu-toggle__controls">
                        <span class="pf-v6-c-menu-toggle__toggle-icon">
                          <svg
                            class="pf-v6-svg"
                            viewBox="0 0 20 20"
                            fill="currentColor"
                            aria-hidden="true"
                            role="img"
                            width="1em"
                            height="1em"
                          >
                            <path
                              d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
                            />
                          </svg>
                        </span>
                      </span>
                    </button>
                  </div>
                  <div
                    class="pf-v6-c-card__title"
                    id="compass-dashboard-grid-events-card-1-title1"
                    style="padding-block-start: 3px;"
                  >
                    <h2 class="pf-v6-c-title pf-m-xl">Events</h2>
                  </div>
                </div>
                <div class="pf-v6-c-card__body">
                  <dl
                    class="pf-v6-c-description-list pf-m-compact"
                    aria-label="Events"
                  >
                    <div class="pf-v6-c-description-list__group">
                      <dt class="pf-v6-c-description-list__term">
                        <div class="pf-v6-l-flex pf-m-nowrap">
                          <div class="pf-v6-l-flex__item pf-m-spacer-sm">
                            <span class="pf-v6-c-icon">
                              <span class="pf-v6-c-icon__content pf-m-danger">
                                <svg
                                  class="pf-v6-svg"
                                  viewBox="0 0 32 32"
                                  fill="currentColor"
                                  aria-hidden="true"
                                  role="img"
                                  width="1em"
                                  height="1em"
                                >
                                  <path
                                    d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm-1.5 8a1.5 1.5 0 1 1 3 0v7a1.5 1.5 0 1 1-3 0V9ZM16 25.001a2 2 0 1 1-.001-3.999A2 2 0 0 1 16 25.001Z"
                                  />
                                </svg>
                              </span>
                            </span>
                          </div>
                          <div class="pf-v6-l-flex__item">Readiness probe failed</div>
                        </div>
                      </dt>
                      <dd class="pf-v6-c-description-list__description">
                        <div
                          class="pf-v6-c-description-list__text"
                        >Readiness probe failed: Get https://10.131.0.7:5000/healthz: dial tcp 10.131.0.7:5000: connect: connection refused</div>
                      </dd>
                      <dd class="pf-v6-c-description-list__description">
                        <div class="pf-v6-c-description-list__text">
                          <time
                            class="pf-v6-u-color-200 pf-v6-u-font-size-sm"
                          >Jun 17, 11:02 am</time>
                        </div>
                      </dd>
                    </div>
                    <div class="pf-v6-c-description-list__group">
                      <dt class="pf-v6-c-description-list__term">
                        <div class="pf-v6-l-flex pf-m-nowrap">
                          <div class="pf-v6-l-flex__item pf-m-spacer-sm">
                            <span class="pf-v6-c-icon">
                              <span class="pf-v6-c-icon__content pf-m-success">
                                <svg
                                  class="pf-v6-svg"
                                  viewBox="0 0 32 32"
                                  fill="currentColor"
                                  aria-hidden="true"
                                  role="img"
                                  width="1em"
                                  height="1em"
                                >
                                  <path
                                    d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                                  />
                                </svg>
                              </span>
                            </span>
                          </div>
                          <div class="pf-v6-l-flex__item">Successful assignment</div>
                        </div>
                      </dt>
                      <dd class="pf-v6-c-description-list__description">
                        <div
                          class="pf-v6-c-description-list__text"
                        >Successfully assigned default/example to ip-10-0-130-149.ec2.internal</div>
                      </dd>
                      <dd class="pf-v6-c-description-list__description">
                        <div class="pf-v6-c-description-list__text">
                          <time
                            class="pf-v6-u-color-200 pf-v6-u-font-size-sm"
                          >Jun 17, 11:13 am</time>
                        </div>
                      </dd>
                    </div>
                    <div class="pf-v6-c-description-list__group">
                      <dt class="pf-v6-c-description-list__term">
                        <div class="pf-v6-l-flex pf-m-nowrap">
                          <div class="pf-v6-l-flex__item pf-m-spacer-sm">
                            <svg
                              class="pf-v6-c-spinner pf-m-md"
                              role="progressbar"
                              viewBox="0 0 100 100"
                              aria-label="Loading"
                            >
                              <circle
                                class="pf-v6-c-spinner__path"
                                cx="50"
                                cy="50"
                                r="45"
                                fill="none"
                              />
                            </svg>
                          </div>
                          <div class="pf-v6-l-flex__item">Pulling image</div>
                        </div>
                      </dt>
                      <dd class="pf-v6-c-description-list__description">
                        <div
                          class="pf-v6-c-description-list__text"
                        >Pulling image "openshift/hello-openshift"</div>
                      </dd>
                      <dd class="pf-v6-c-description-list__description">
                        <div class="pf-v6-c-description-list__text">
                          <time
                            class="pf-v6-u-color-200 pf-v6-u-font-size-sm"
                          >Jun 17, 10:59 am</time>
                        </div>
                      </dd>
                    </div>
                    <div class="pf-v6-c-description-list__group">
                      <dt class="pf-v6-c-description-list__term">
                        <div class="pf-v6-l-flex pf-m-nowrap">
                          <div class="pf-v6-l-flex__item pf-m-spacer-sm">
                            <span class="pf-v6-c-icon">
                              <span class="pf-v6-c-icon__content pf-m-success">
                                <svg
                                  class="pf-v6-svg"
                                  viewBox="0 0 32 32"
                                  fill="currentColor"
                                  aria-hidden="true"
                                  role="img"
                                  width="1em"
                                  height="1em"
                                >
                                  <path
                                    d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                                  />
                                </svg>
                              </span>
                            </span>
                          </div>
                          <div class="pf-v6-l-flex__item">Created container</div>
                        </div>
                      </dt>
                      <dd class="pf-v6-c-description-list__description">
                        <div
                          class="pf-v6-c-description-list__text"
                        >Created container hello-openshift</div>
                      </dd>
                      <dd class="pf-v6-c-description-list__description">
                        <div class="pf-v6-c-description-list__text">
                          <time
                            class="pf-v6-u-color-200 pf-v6-u-font-size-sm"
                          >Jun 17, 10:45 am</time>
                        </div>
                      </dd>
                    </div>

                    <div class="pf-v6-c-description-list__group">
                      <dt class="pf-v6-c-description-list__term">
                        <div class="pf-v6-l-flex pf-m-nowrap">
                          <div class="pf-v6-l-flex__item pf-m-spacer-sm">
                            <span class="pf-v6-c-icon">
                              <span class="pf-v6-c-icon__content pf-m-warning">
                                <svg
                                  class="pf-v6-svg"
                                  viewBox="0 0 32 32"
                                  fill="currentColor"
                                  aria-hidden="true"
                                  role="img"
                                  width="1em"
                                  height="1em"
                                >
                                  <path
                                    d="m31.874 28.514-15.011-27a1.001 1.001 0 0 0-1.748 0l-15.011 27A1 1 0 0 0 .978 30H31a1 1 0 0 0 .874-1.486ZM14.5 12a1.5 1.5 0 0 1 3 0v5a1.5 1.5 0 0 1-3 0v-5ZM16 26.001a2 2 0 1 1-.001-3.999A2 2 0 0 1 16 26.001Z"
                                  />
                                </svg>
                              </span>
                            </span>
                          </div>
                          <div
                            class="pf-v6-l-flex__item"
                          >CPU utilitization over 50%</div>
                        </div>
                      </dt>
                      <dd class="pf-v6-c-description-list__description">
                        <div
                          class="pf-v6-c-description-list__text"
                        >Migrated 2 pods to other hosts</div>
                      </dd>
                      <dd class="pf-v6-c-description-list__description">
                        <div class="pf-v6-c-description-list__text">
                          <time
                            class="pf-v6-u-color-200 pf-v6-u-font-size-sm"
                          >Jun 17, 10:33 am</time>
                        </div>
                      </dd>
                    </div>

                    <div class="pf-v6-c-description-list__group">
                      <dt class="pf-v6-c-description-list__term">
                        <div class="pf-v6-l-flex pf-m-nowrap">
                          <div class="pf-v6-l-flex__item pf-m-spacer-sm">
                            <span class="pf-v6-c-icon">
                              <span class="pf-v6-c-icon__content pf-m-danger">
                                <svg
                                  class="pf-v6-svg"
                                  viewBox="0 0 32 32"
                                  fill="currentColor"
                                  aria-hidden="true"
                                  role="img"
                                  width="1em"
                                  height="1em"
                                >
                                  <path
                                    d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm-1.5 8a1.5 1.5 0 1 1 3 0v7a1.5 1.5 0 1 1-3 0V9ZM16 25.001a2 2 0 1 1-.001-3.999A2 2 0 0 1 16 25.001Z"
                                  />
                                </svg>
                              </span>
                            </span>
                          </div>
                          <div class="pf-v6-l-flex__item">Rook-osd-10-328949</div>
                        </div>
                      </dt>
                      <dd class="pf-v6-c-description-list__description">
                        <div
                          class="pf-v6-c-description-list__text"
                        >Rebuild initiated as Disk 5 failed</div>
                      </dd>
                      <dd class="pf-v6-c-description-list__description">
                        <div class="pf-v6-c-description-list__text">
                          <time
                            class="pf-v6-u-color-200 pf-v6-u-font-size-sm"
                          >Jun 17, 10:33 am</time>
                        </div>
                      </dd>
                    </div>

                    <div class="pf-v6-c-description-list__group">
                      <dt class="pf-v6-c-description-list__term">
                        <div class="pf-v6-l-flex pf-m-nowrap">
                          <div class="pf-v6-l-flex__item pf-m-spacer-sm">
                            <span class="pf-v6-c-icon">
                              <span class="pf-v6-c-icon__content pf-m-success">
                                <svg
                                  class="pf-v6-svg"
                                  viewBox="0 0 32 32"
                                  fill="currentColor"
                                  aria-hidden="true"
                                  role="img"
                                  width="1em"
                                  height="1em"
                                >
                                  <path
                                    d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                                  />
                                </svg>
                              </span>
                            </span>
                          </div>
                          <div class="pf-v6-l-flex__item">Created container</div>
                        </div>
                      </dt>
                      <dd class="pf-v6-c-description-list__description">
                        <div
                          class="pf-v6-c-description-list__text"
                        >Created container hello-openshift-123</div>
                      </dd>
                      <dd class="pf-v6-c-description-list__description">
                        <div class="pf-v6-c-description-list__text">
                          <time
                            class="pf-v6-u-color-200 pf-v6-u-font-size-sm"
                          >Jun 17, 10:31 am</time>
                        </div>
                      </dd>
                    </div>

                    <div class="pf-v6-c-description-list__group">
                      <dt class="pf-v6-c-description-list__term">
                        <div class="pf-v6-l-flex pf-m-nowrap">
                          <div class="pf-v6-l-flex__item pf-m-spacer-sm">
                            <span class="pf-v6-c-icon">
                              <span class="pf-v6-c-icon__content pf-m-success">
                                <svg
                                  class="pf-v6-svg"
                                  viewBox="0 0 32 32"
                                  fill="currentColor"
                                  aria-hidden="true"
                                  role="img"
                                  width="1em"
                                  height="1em"
                                >
                                  <path
                                    d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                                  />
                                </svg>
                              </span>
                            </span>
                          </div>
                          <div class="pf-v6-l-flex__item">Created container</div>
                        </div>
                      </dt>
                      <dd class="pf-v6-c-description-list__description">
                        <div
                          class="pf-v6-c-description-list__text"
                        >Created container hello-openshift-456</div>
                      </dd>
                      <dd class="pf-v6-c-description-list__description">
                        <div class="pf-v6-c-description-list__text">
                          <time
                            class="pf-v6-u-color-200 pf-v6-u-font-size-sm"
                          >Jun 17, 10:30 am</time>
                        </div>
                      </dd>
                    </div>
                  </dl>
                </div>
                <hr class="pf-v6-c-divider" />
                <div class="pf-v6-c-card__footer">
                  <a href="#">View all events</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-compass__main-footer pf-m-expanded">
        <div class="pf-v6-c-compass__message-bar">
          <div class="pf-v6-c-panel pf-m-pill pf-m-glass pf-m-no-border">
            <div class="pf-v6-c-panel__main">chatbot message bar</div>
          </div>
        </div>
      </div>
    </div>
    <div class="pf-v6-c-compass__sidebar pf-m-expanded pf-m-end">
      <div class="pf-v6-c-panel pf-m-pill pf-m-glass">
        <div class="pf-v6-c-panel__main">
          <div class="pf-v6-c-panel__main-body">
            <div class="pf-v6-c-action-list pf-m-icons pf-m-vertical">
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="Notifications"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M28 21c-1.103 0-2-.897-2-2v-4c0-4.885-3.523-8.955-8.159-9.823.405-.445.659-1.03.659-1.677C18.5 2.122 17.379 1 16 1s-2.5 1.122-2.5 2.5c0 .647.254 1.233.659 1.677C9.523 6.045 6 10.115 6 15v4c0 1.103-.897 2-2 2a1 1 0 0 0-1 1v3.5c0 .827.673 1.5 1.5 1.5H12c0 2.206 1.794 4 4 4s4-1.794 4-4h7.5c.827 0 1.5-.673 1.5-1.5V22a1 1 0 0 0-1-1Zm-1 4H5v-2.126A4.006 4.006 0 0 0 8 19v-4c0-4.411 3.589-8 8-8s8 3.589 8 8v4a4.008 4.008 0 0 0 3 3.874V25Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="List"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M31 16a1 1 0 0 1-1 1H9a1 1 0 0 1 0-2h21a1 1 0 0 1 1 1Zm-1 9H9a1 1 0 0 0 0 2h21a1 1 0 0 0 0-2ZM9 7h21a1 1 0 0 0 0-2H9a1 1 0 0 0 0 2ZM2 4.51a1.5 1.5 0 1 0 .001 3.001A1.5 1.5 0 0 0 2 4.51Zm0 10a1.5 1.5 0 1 0 .001 3.001A1.5 1.5 0 0 0 2 14.51Zm0 10a1.5 1.5 0 1 0 .001 3.001A1.5 1.5 0 0 0 2 24.51Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="Zap"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M15 31a1 1 0 0 1-1-1V19h-4a.999.999 0 0 1-.916-1.401l7-16A1 1 0 0 1 18 2v11h4a.999.999 0 0 1 .916 1.401l-7 16A.998.998 0 0 1 15 31Zm-3.471-14H14.5c.827 0 1.5.673 1.5 1.5v6.719L20.471 15H17.5c-.827 0-1.5-.673-1.5-1.5V6.781L11.529 17Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="Download"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M30 29a1 1 0 0 1-1 1H3a1 1 0 0 1 0-2h26a1 1 0 0 1 1 1Zm-15.061-4.646c.292.292.676.438 1.061.438s.768-.146 1.061-.438l8.646-8.646a.999.999 0 1 0-1.414-1.414L17 21.587V3a1 1 0 0 0-2 0v18.586l-7.293-7.293a.999.999 0 1 0-1.414 1.414l8.646 8.646Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="Help"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

```

### Multiple sections

This demo places multiple sections within the main Compass section, with each section containing a card view.

Without a glass panel component wrapping all of the content, there is no rounded-rectangle container as the main content background. Instead, the `.pf-v6-c-compass__content` is a grid with 2 independently scrollable glass panel components.

```html isFullscreen isBeta
<div class="pf-v6-c-compass pf-m-animate-smoothly">
  <div class="pf-v6-c-compass__container">
    <div class="pf-v6-c-compass__header pf-m-expanded">
      <div class="pf-v6-c-compass__logo">
        <svg
          width="192"
          height="39"
          viewBox="0 0 192 39"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          aria-hidden="true"
        >
          <path
            d="M33.3807 22.9001C36.6672 22.9001 41.4287 22.2167 41.4287 18.2926C41.4287 17.9865 41.4209 17.6883 41.3472 17.3901L39.3885 8.85069C38.9336 6.97444 38.5392 6.11944 35.2501 4.47014C32.7023 3.16125 27.1468 1 25.5035 1C23.9733 1 23.5211 2.98972 21.7069 2.98972C19.8927 2.98972 18.6465 1.51194 17.0032 1.51194C15.3599 1.51194 14.395 2.59389 13.6036 4.81056C13.6036 4.81056 11.3924 11.0674 11.1085 11.9778C11.0506 12.1493 11.0506 12.3393 11.0506 12.4897C11.0506 14.9228 20.5921 22.9001 33.3833 22.9001M41.9414 19.8839C42.3963 22.0451 42.3963 22.2721 42.3963 22.5571C42.3963 26.2542 38.2579 28.3019 32.818 28.3019C20.5185 28.3019 9.74918 21.0767 9.74918 16.3003C9.74918 15.5614 9.92008 14.8779 10.1462 14.366C5.72383 14.5929 0 15.3899 0 20.4539C0 28.7585 19.6114 39 35.1396 39C47.0421 39 50.0447 33.5956 50.0447 29.3285C50.0447 25.9718 47.1552 22.1612 41.9388 19.8839"
            fill="#EE0000"
          />
          <path
            d="M41.9386 19.8864C42.3935 22.0477 42.3935 22.2746 42.3935 22.5596C42.3935 26.2567 38.255 28.3045 32.8152 28.3045C20.5157 28.3045 9.74634 21.0792 9.74634 16.3028C9.74634 15.5639 9.91724 14.8804 10.1434 14.3685L11.1083 11.9777C11.0504 12.1492 11.0504 12.3392 11.0504 12.4896C11.0504 14.9227 20.5919 22.9 33.3831 22.9C36.6696 22.9 41.4312 22.2165 41.4312 18.2925C41.4312 17.9864 41.4233 17.6882 41.3496 17.39L41.9412 19.8864H41.9386Z"
            fill="black"
          />
          <path
            d="M75.764 16V1.29995H82.295C83.261 1.29995 84.115 1.48895 84.857 1.86695C85.599 2.24495 86.173 2.76995 86.579 3.44195C86.999 4.09995 87.209 4.86995 87.209 5.75195C87.209 6.70395 86.943 7.53695 86.411 8.25095C85.893 8.95095 85.186 9.46195 84.29 9.78395L87.398 16H84.605L81.77 10.12H78.284V16H75.764ZM78.284 8.10395H82.064C82.848 8.10395 83.478 7.89395 83.954 7.47395C84.43 7.03995 84.668 6.47295 84.668 5.77295C84.668 5.05895 84.43 4.49195 83.954 4.07195C83.478 3.63795 82.848 3.42095 82.064 3.42095H78.284V8.10395Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M93.9392 16.21C92.9312 16.21 92.0212 15.972 91.2092 15.496C90.3972 15.006 89.7532 14.3549 89.2772 13.5429C88.8012 12.7169 88.5632 11.7859 88.5632 10.75C88.5632 9.71395 88.7872 8.78995 89.2352 7.97795C89.6832 7.16595 90.2922 6.52195 91.0622 6.04595C91.8462 5.55595 92.7142 5.31095 93.6662 5.31095C94.6462 5.31095 95.5072 5.54895 96.2492 6.02495C97.0052 6.50095 97.5932 7.14495 98.0132 7.95695C98.4472 8.76895 98.6642 9.69995 98.6642 10.75V11.3169H90.8942C90.9782 11.8909 91.1602 12.4019 91.4402 12.8499C91.7342 13.2839 92.1052 13.627 92.5532 13.879C93.0152 14.1309 93.5122 14.257 94.0442 14.257C94.5342 14.257 94.9962 14.173 95.4302 14.005C95.8782 13.823 96.2492 13.578 96.5432 13.2699L98.0972 14.677C97.4532 15.209 96.7952 15.601 96.1232 15.853C95.4652 16.091 94.7372 16.21 93.9392 16.21ZM90.9152 9.84695H96.4172C96.3332 9.34295 96.1582 8.89495 95.8922 8.50295C95.6402 8.11095 95.3182 7.80295 94.9262 7.57895C94.5482 7.35495 94.1282 7.24295 93.6662 7.24295C93.2042 7.24295 92.7772 7.35495 92.3852 7.57895C92.0072 7.78895 91.6922 8.08995 91.4402 8.48195C91.1882 8.87395 91.0132 9.32895 90.9152 9.84695Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M105.388 16.1049C104.506 16.1049 103.708 15.867 102.994 15.391C102.28 14.901 101.706 14.257 101.272 13.459C100.852 12.6469 100.642 11.7439 100.642 10.75C100.642 9.74195 100.859 8.83895 101.293 8.04095C101.727 7.22895 102.315 6.58495 103.057 6.10895C103.813 5.63295 104.646 5.39495 105.556 5.39495C106.158 5.39495 106.718 5.51395 107.236 5.75195C107.768 5.97595 108.23 6.31195 108.622 6.75995V0.94295L110.995 0.522949V16H108.643V14.6139C108.265 15.0899 107.796 15.461 107.236 15.727C106.676 15.979 106.06 16.1049 105.388 16.1049ZM106.123 14.11C106.627 14.11 107.096 14.012 107.53 13.816C107.964 13.606 108.328 13.319 108.622 12.955V8.52395C108.314 8.15995 107.943 7.87995 107.509 7.68395C107.075 7.48795 106.613 7.38995 106.123 7.38995C105.521 7.38995 104.982 7.53695 104.506 7.83095C104.044 8.11095 103.673 8.50295 103.393 9.00695C103.113 9.51095 102.973 10.092 102.973 10.75C102.973 11.38 103.113 11.9539 103.393 12.4719C103.673 12.976 104.044 13.375 104.506 13.669C104.982 13.9629 105.521 14.11 106.123 14.11Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M118.848 16V1.29995H121.368V7.47395H128.676V1.29995H131.196V16H128.676V9.72095H121.368V16H118.848Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M137.314 16.189C136.586 16.189 135.935 16.056 135.361 15.79C134.801 15.51 134.36 15.132 134.038 14.656C133.73 14.166 133.576 13.606 133.576 12.976C133.576 12.346 133.737 11.7999 134.059 11.3379C134.395 10.8759 134.864 10.519 135.466 10.267C136.068 10.015 136.782 9.88895 137.608 9.88895C138.098 9.88895 138.581 9.94495 139.057 10.0569C139.533 10.1549 139.995 10.323 140.443 10.561V9.38495C140.443 8.68495 140.24 8.15995 139.834 7.80995C139.442 7.45995 138.84 7.28495 138.028 7.28495C137.594 7.28495 137.125 7.35495 136.621 7.49495C136.131 7.62095 135.578 7.82395 134.962 8.10395L134.122 6.38195C135.662 5.66795 137.118 5.31095 138.49 5.31095C139.862 5.31095 140.919 5.64695 141.661 6.31895C142.417 6.97695 142.795 7.91495 142.795 9.13295V16H140.443V14.908C139.995 15.342 139.512 15.6639 138.994 15.874C138.476 16.084 137.916 16.189 137.314 16.189ZM135.802 12.934C135.802 13.424 135.998 13.809 136.39 14.089C136.782 14.3689 137.307 14.509 137.965 14.509C138.441 14.509 138.882 14.439 139.288 14.299C139.708 14.1449 140.093 13.9209 140.443 13.627V11.926C140.079 11.7579 139.701 11.6319 139.309 11.5479C138.917 11.464 138.49 11.422 138.028 11.422C137.342 11.422 136.796 11.5549 136.39 11.8209C135.998 12.0869 135.802 12.458 135.802 12.934Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M149.897 16.21C148.833 16.21 148.028 15.9649 147.482 15.4749C146.936 14.971 146.663 14.236 146.663 13.2699V7.36895H144.563V5.47895H146.663V2.58095L149.036 2.07695V5.47895H151.955V7.36895H149.036V12.745C149.036 13.2629 149.148 13.634 149.372 13.858C149.596 14.068 149.974 14.1729 150.506 14.1729C150.744 14.1729 150.961 14.1589 151.157 14.1309C151.367 14.089 151.626 14.0189 151.934 13.9209V15.9159C151.64 16.0139 151.304 16.084 150.926 16.1259C150.562 16.1819 150.219 16.21 149.897 16.21Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M73.916 38L79.964 23.2999H83.471L89.456 38H86.159L84.668 34.1359H78.599L77.087 38H73.916ZM79.544 31.6999H83.744L81.644 26.2819L79.544 31.6999Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M94.4493 38.2099C93.6093 38.2099 92.8603 38.028 92.2023 37.664C91.5583 37.286 91.0473 36.768 90.6693 36.11C90.3053 35.452 90.1233 34.6959 90.1233 33.8419V27.059H93.0003V33.422C93.0003 34.122 93.2033 34.682 93.6093 35.102C94.0293 35.522 94.5823 35.7319 95.2683 35.7319C96.2483 35.7319 97.0043 35.368 97.5363 34.6399V27.059H100.413V38H97.5363V37.118C96.6963 37.846 95.6673 38.2099 94.4493 38.2099Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M107.842 38.1679C106.625 38.1679 105.7 37.895 105.07 37.3489C104.454 36.7889 104.146 35.9769 104.146 34.9129V29.4529H101.899V27.059H104.146V24.2659L107.024 23.6149V27.059H110.153V29.4529H107.024V34.325C107.024 34.829 107.136 35.193 107.36 35.417C107.583 35.6269 107.975 35.7319 108.535 35.7319C108.815 35.7319 109.068 35.7179 109.292 35.6899C109.529 35.6479 109.789 35.5779 110.069 35.4799V37.853C109.775 37.951 109.404 38.028 108.956 38.084C108.522 38.1399 108.15 38.1679 107.842 38.1679Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M116.767 38.2099C115.675 38.2099 114.688 37.958 113.806 37.4539C112.924 36.9499 112.224 36.271 111.706 35.417C111.188 34.563 110.929 33.604 110.929 32.54C110.929 31.476 111.188 30.517 111.706 29.663C112.224 28.795 112.924 28.1089 113.806 27.6049C114.688 27.101 115.675 26.8489 116.767 26.8489C117.859 26.8489 118.846 27.101 119.728 27.6049C120.61 28.1089 121.31 28.795 121.828 29.663C122.346 30.517 122.605 31.476 122.605 32.54C122.605 33.604 122.346 34.563 121.828 35.417C121.31 36.271 120.61 36.9499 119.728 37.4539C118.846 37.958 117.859 38.2099 116.767 38.2099ZM116.767 35.7109C117.341 35.7109 117.852 35.5709 118.3 35.291C118.762 35.011 119.126 34.6329 119.392 34.1569C119.672 33.6669 119.812 33.128 119.812 32.54C119.812 31.938 119.672 31.399 119.392 30.923C119.126 30.447 118.762 30.069 118.3 29.7889C117.852 29.4949 117.341 29.3479 116.767 29.3479C116.207 29.3479 115.696 29.4949 115.234 29.7889C114.772 30.069 114.408 30.447 114.142 30.923C113.876 31.399 113.743 31.938 113.743 32.54C113.743 33.128 113.876 33.6669 114.142 34.1569C114.408 34.6329 114.772 35.011 115.234 35.291C115.696 35.5709 116.207 35.7109 116.767 35.7109Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M124.373 38V27.059H127.25V27.8989C128.034 27.1989 128.986 26.8489 130.106 26.8489C130.82 26.8489 131.457 26.996 132.017 27.2899C132.577 27.57 133.039 27.969 133.403 28.4869C134.313 27.3949 135.517 26.8489 137.015 26.8489C137.841 26.8489 138.562 27.038 139.178 27.416C139.808 27.78 140.298 28.291 140.648 28.9489C141.012 29.5929 141.194 30.3489 141.194 31.2169V38H138.338V31.6369C138.338 30.9229 138.149 30.3629 137.771 29.9569C137.393 29.5369 136.889 29.327 136.259 29.327C135.377 29.327 134.677 29.6909 134.159 30.4189C134.173 30.5449 134.187 30.6709 134.201 30.7969C134.215 30.9229 134.222 31.063 134.222 31.2169V38H131.345V31.6369C131.345 30.9229 131.156 30.3629 130.778 29.9569C130.414 29.5369 129.917 29.327 129.287 29.327C128.405 29.327 127.726 29.6629 127.25 30.3349V38H124.373Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M146.87 38.1889C146.086 38.1889 145.393 38.049 144.791 37.769C144.189 37.475 143.72 37.076 143.384 36.5719C143.048 36.0679 142.88 35.4869 142.88 34.8289C142.88 33.7789 143.272 32.9669 144.056 32.393C144.854 31.805 145.946 31.511 147.332 31.511C148.284 31.511 149.18 31.6579 150.02 31.952V31.1539C150.02 29.8799 149.25 29.243 147.71 29.243C147.248 29.243 146.751 29.32 146.219 29.4739C145.687 29.6139 145.071 29.8379 144.371 30.146L143.321 28.025C144.189 27.6329 145.015 27.3389 145.799 27.143C146.597 26.947 147.395 26.8489 148.193 26.8489C149.663 26.8489 150.804 27.2059 151.616 27.92C152.442 28.62 152.855 29.6139 152.855 30.9019V38H150.02V37.2229C149.572 37.5589 149.089 37.804 148.571 37.958C148.053 38.1119 147.486 38.1889 146.87 38.1889ZM145.61 34.7659C145.61 35.186 145.792 35.5219 146.156 35.7739C146.52 36.0119 147.003 36.131 147.605 36.131C148.571 36.131 149.376 35.893 150.02 35.417V33.8209C149.32 33.541 148.55 33.401 147.71 33.401C147.052 33.401 146.534 33.527 146.156 33.7789C145.792 34.0169 145.61 34.346 145.61 34.7659Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M159.912 38.1679C158.694 38.1679 157.77 37.895 157.14 37.3489C156.524 36.7889 156.216 35.9769 156.216 34.9129V29.4529H153.969V27.059H156.216V24.2659L159.093 23.6149V27.059H162.222V29.4529H159.093V34.325C159.093 34.829 159.205 35.193 159.429 35.417C159.653 35.6269 160.045 35.7319 160.605 35.7319C160.885 35.7319 161.137 35.7179 161.361 35.6899C161.599 35.6479 161.858 35.5779 162.138 35.4799V37.853C161.844 37.951 161.473 38.028 161.025 38.084C160.591 38.1399 160.22 38.1679 159.912 38.1679Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M163.625 38V27.059H166.502V38H163.625ZM165.053 25.757C164.605 25.757 164.22 25.596 163.898 25.274C163.576 24.952 163.415 24.5669 163.415 24.1189C163.415 23.6569 163.576 23.2719 163.898 22.9639C164.22 22.6419 164.605 22.4809 165.053 22.4809C165.515 22.4809 165.9 22.6419 166.208 22.9639C166.53 23.2719 166.691 23.6569 166.691 24.1189C166.691 24.5669 166.53 24.952 166.208 25.274C165.9 25.596 165.515 25.757 165.053 25.757Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M174.086 38.2099C172.994 38.2099 172.007 37.958 171.125 37.4539C170.243 36.9499 169.543 36.271 169.025 35.417C168.507 34.563 168.248 33.604 168.248 32.54C168.248 31.476 168.507 30.517 169.025 29.663C169.543 28.795 170.243 28.1089 171.125 27.6049C172.007 27.101 172.994 26.8489 174.086 26.8489C175.178 26.8489 176.165 27.101 177.047 27.6049C177.929 28.1089 178.629 28.795 179.147 29.663C179.665 30.517 179.924 31.476 179.924 32.54C179.924 33.604 179.665 34.563 179.147 35.417C178.629 36.271 177.929 36.9499 177.047 37.4539C176.165 37.958 175.178 38.2099 174.086 38.2099ZM174.086 35.7109C174.66 35.7109 175.171 35.5709 175.619 35.291C176.081 35.011 176.445 34.6329 176.711 34.1569C176.991 33.6669 177.131 33.128 177.131 32.54C177.131 31.938 176.991 31.399 176.711 30.923C176.445 30.447 176.081 30.069 175.619 29.7889C175.171 29.4949 174.66 29.3479 174.086 29.3479C173.526 29.3479 173.015 29.4949 172.553 29.7889C172.091 30.069 171.727 30.447 171.461 30.923C171.195 31.399 171.062 31.938 171.062 32.54C171.062 33.128 171.195 33.6669 171.461 34.1569C171.727 34.6329 172.091 35.011 172.553 35.291C173.015 35.5709 173.526 35.7109 174.086 35.7109Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <path
            d="M181.693 38V27.059H184.57V27.962C185.396 27.2199 186.418 26.8489 187.636 26.8489C188.49 26.8489 189.239 27.038 189.883 27.416C190.541 27.78 191.052 28.291 191.416 28.9489C191.78 29.5929 191.962 30.3489 191.962 31.2169V38H189.085V31.6369C189.085 30.9229 188.882 30.3629 188.476 29.9569C188.07 29.5369 187.517 29.327 186.817 29.327C186.327 29.327 185.893 29.425 185.515 29.621C185.137 29.803 184.822 30.0689 184.57 30.4189V38H181.693Z"
            fill="var(--pf-t--global--text--color--regular)"
          />
          <line
            x1="66.5"
            y1="1.5"
            x2="66.5"
            y2="38.5"
            stroke="var(--pf-t--global--text--color--regular)"
            stroke-linecap="round"
          />
        </svg>
      </div>
      <div class="pf-v6-c-compass__nav">
        <div class="pf-v6-c-panel pf-m-pill pf-m-glass">
          <div class="pf-v6-c-panel__main">
            <div class="pf-v6-c-panel__main-body">
              <div class="pf-v6-c-compass__nav-content">
                <div class="pf-v6-c-compass__nav-home">
                  <button
                    class="pf-v6-c-button pf-m-circle pf-m-plain"
                    type="button"
                    aria-label="Home"
                  >
                    <span class="pf-v6-c-button__icon">
                      <svg
                        class="pf-v6-svg"
                        viewBox="0 0 32 32"
                        fill="currentColor"
                        aria-hidden="true"
                        role="img"
                        width="1em"
                        height="1em"
                      >
                        <path
                          d="M30.707 15.435 17.061 1.789a1.501 1.501 0 0 0-2.121 0L1.293 15.435a.999.999 0 1 0 1.414 1.414L3 16.556V29.5c0 .827.673 1.5 1.5 1.5h23c.827 0 1.5-.673 1.5-1.5V16.556l.293.293a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414ZM19 29h-6V19h6v10Zm8-10v10h-6V18.5c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5V29H5V14.556l11-11 11 11V19Z"
                        />
                      </svg>
                    </span>
                  </button>
                </div>
                <div class="pf-v6-c-compass__nav-main">
                  <nav
                    class="pf-v6-c-tabs pf-m-nav"
                    aria-label="Compass primary"
                  >
                    <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
                      <button
                        class="pf-v6-c-button pf-m-small pf-m-plain"
                        type="button"
                        aria-label="Scroll left"
                        disabled
                      >
                        <span class="pf-v6-c-button__icon">
                          <svg
                            class="pf-v6-svg"
                            viewBox="0 0 20 20"
                            fill="currentColor"
                            aria-hidden="true"
                            role="img"
                            width="1em"
                            height="1em"
                          >
                            <path
                              d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                            />
                          </svg>
                        </span>
                      </button>
                    </div>
                    <ul
                      class="pf-v6-c-tabs__list"
                      role="tablist"
                      aria-label="Compass primary"
                    >
                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="primary-nav-users-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Users</span>
                        </a>
                      </li>
                      <li
                        class="pf-v6-c-tabs__item pf-m-current"
                        role="presentation"
                      >
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="true"
                          id="primary-nav-containers-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Containers</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="primary-nav-database-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Database</span>
                        </a>
                      </li>

                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="primary-nav-server-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Server</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="primary-nav-system-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">System</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="primary-nav-network-wired-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Network</span>
                        </a>
                      </li>
                    </ul>

                    <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
                      <button
                        class="pf-v6-c-button pf-m-small pf-m-plain"
                        type="button"
                        aria-label="Scroll right"
                        disabled
                      >
                        <span class="pf-v6-c-button__icon">
                          <svg
                            class="pf-v6-svg"
                            viewBox="0 0 20 20"
                            fill="currentColor"
                            aria-hidden="true"
                            role="img"
                            width="1em"
                            height="1em"
                          >
                            <path
                              d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                            />
                          </svg>
                        </span>
                      </button>
                    </div>
                  </nav>
                </div>
                <div class="pf-v6-c-compass__nav-search">
                  <button
                    class="pf-v6-c-button pf-m-circle pf-m-plain"
                    type="button"
                    aria-label="Search"
                  >
                    <span class="pf-v6-c-button__icon">
                      <svg
                        class="pf-v6-svg"
                        viewBox="0 0 32 32"
                        fill="currentColor"
                        aria-hidden="true"
                        role="img"
                        width="1em"
                        height="1em"
                      >
                        <path
                          d="m30.796 29.205-8.557-8.557A11.945 11.945 0 0 0 25 13c0-6.617-5.383-12-12-12S1 6.383 1 13s5.383 12 12 12c2.904 0 5.57-1.038 7.648-2.761l8.556 8.556a1.122 1.122 0 0 0 1.592 0 1.127 1.127 0 0 0 0-1.591ZM3 13C3 7.486 7.486 3 13 3s10 4.486 10 10-4.486 10-10 10S3 18.514 3 13Z"
                        />
                      </svg>
                    </span>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="pf-v6-c-panel pf-m-pill pf-m-glass">
          <div class="pf-v6-c-panel__main">
            <div class="pf-v6-c-panel__main-body">
              <div class="pf-v6-c-compass__nav-content">
                <div class="pf-v6-c-compass__nav-main">
                  <nav
                    class="pf-v6-c-tabs pf-m-nav pf-m-subtab"
                    aria-label="Compass secondary"
                  >
                    <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
                      <button
                        class="pf-v6-c-button pf-m-small pf-m-plain"
                        type="button"
                        aria-label="Scroll left"
                        disabled
                      >
                        <span class="pf-v6-c-button__icon">
                          <svg
                            class="pf-v6-svg"
                            viewBox="0 0 20 20"
                            fill="currentColor"
                            aria-hidden="true"
                            role="img"
                            width="1em"
                            height="1em"
                          >
                            <path
                              d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                            />
                          </svg>
                        </span>
                      </button>
                    </div>
                    <ul
                      class="pf-v6-c-tabs__list"
                      role="tablist"
                      aria-label="Compass secondary"
                    >
                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="secondary-nav-sub-1-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Item 1</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="secondary-nav-sub-2-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Item 2</span>
                        </a>
                      </li>
                      <li
                        class="pf-v6-c-tabs__item pf-m-current"
                        role="presentation"
                      >
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="true"
                          id="secondary-nav-sub-3-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Item 3</span>
                        </a>
                      </li>

                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link pf-m-disabled"
                          aria-disabled="true"
                          tabindex="-1"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="secondary-nav-sub-disabled-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Disabled</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link pf-m-aria-disabled"
                          aria-disabled="true"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="secondary-nav-sub-aria-disabled-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-tabs__item" role="presentation">
                        <a
                          class="pf-v6-c-tabs__link"
                          href="#"
                          role="tab"
                          aria-selected="false"
                          id="secondary-nav-sub-6-link"
                        >
                          <span class="pf-v6-c-tabs__item-text">Item 6</span>
                        </a>
                      </li>
                    </ul>

                    <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
                      <button
                        class="pf-v6-c-button pf-m-small pf-m-plain"
                        type="button"
                        aria-label="Scroll right"
                        disabled
                      >
                        <span class="pf-v6-c-button__icon">
                          <svg
                            class="pf-v6-svg"
                            viewBox="0 0 20 20"
                            fill="currentColor"
                            aria-hidden="true"
                            role="img"
                            width="1em"
                            height="1em"
                          >
                            <path
                              d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                            />
                          </svg>
                        </span>
                      </button>
                    </div>
                  </nav>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-compass__profile">
        <button
          class="pf-v6-c-menu-toggle pf-m-circle pf-m-text pf-m-plain"
          type="button"
          aria-expanded="false"
        >
          <span class="pf-v6-c-menu-toggle__icon">
            <img
              class="pf-v6-c-avatar pf-m-md"
              alt="Avatar image"
              src="/assets/images/img_avatar-light.svg"
            />
          </span>
          <span class="pf-v6-c-menu-toggle__text">Ned Username</span>
          <span class="pf-v6-c-menu-toggle__controls">
            <span class="pf-v6-c-menu-toggle__toggle-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </div>
    </div>
    <div class="pf-v6-c-compass__sidebar pf-m-expanded pf-m-start">
      <div class="pf-v6-c-panel pf-m-pill pf-m-glass">
        <div class="pf-v6-c-panel__main">
          <div class="pf-v6-c-panel__main-body">
            <div class="pf-v6-c-action-list pf-m-icons pf-m-vertical">
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="Add"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M28.5 2h-25C2.673 2 2 2.673 2 3.5v25c0 .827.673 1.5 1.5 1.5h25c.827 0 1.5-.673 1.5-1.5v-25c0-.827-.673-1.5-1.5-1.5ZM28 28H4V4h24v24ZM8 16a1 1 0 0 1 1-1h6V9a1 1 0 1 1 2 0v6h6a1 1 0 1 1 0 2h-6v6a1 1 0 1 1-2 0v-6H9a1 1 0 0 1-1-1Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="Collections"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M28.5 11h-25c-.827 0-1.5.673-1.5 1.5v17c0 .827.673 1.5 1.5 1.5h25c.827 0 1.5-.673 1.5-1.5v-17c0-.827-.673-1.5-1.5-1.5ZM28 29H4V13h24v16ZM6 2a1 1 0 0 1 1-1h18a1 1 0 0 1 0 2H7a1 1 0 0 1-1-1ZM4 7a1 1 0 0 1 1-1h22a1 1 0 0 1 0 2H5a1 1 0 0 1-1-1Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-v6-m-ai-indicator pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="AI assistant"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M30.502 7c0 .29-.209.536-.498.59a5.523 5.523 0 0 0-4.417 4.417c-.054.289-.3.498-.59.498s-.536-.21-.59-.498A5.52 5.52 0 0 0 19.99 7.59c-.289-.054-.498-.3-.498-.59s.21-.536.498-.59a5.52 5.52 0 0 0 4.417-4.417c.054-.289.301-.498.59-.498s.536.21.59.498a5.523 5.523 0 0 0 4.417 4.417c.289.054.498.3.498.59Zm-4.465 9.962A11.932 11.932 0 0 1 15.038 5.97C15.001 5.447 14.524 5 14 5c-.521 0-.997.442-1.038.962a11.932 11.932 0 0 1-10.992 11C1.447 16.999 1 17.476 1 18c0 .521.442.997.962 1.038a11.932 11.932 0 0 1 11 10.992c.037.524.514.97 1.038.97.521 0 .997-.442 1.038-.962a11.933 11.933 0 0 1 11-10.999c.519-.042.961-.516.961-1.038 0-.521-.442-.997-.962-1.038Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="Volume"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M17.439 2.102a1 1 0 0 0-1.054.109L7.656 9H2.5C1.673 9 1 9.673 1 10.5v11c0 .827.673 1.5 1.5 1.5h5.157l8.729 6.789a.998.998 0 0 0 1.053.109c.343-.168.561-.517.561-.898V3a1 1 0 0 0-.561-.898ZM16 26.955l-7.386-5.744A1 1 0 0 0 8 21H3V11h5a.997.997 0 0 0 .614-.211L16 5.045v21.91ZM31 16a14.94 14.94 0 0 1-4.284 10.488.997.997 0 0 1-1.414.018 1 1 0 0 1-.018-1.414C27.68 22.637 29 19.408 29 16s-1.319-6.637-3.716-9.092a.999.999 0 1 1 1.432-1.396A14.94 14.94 0 0 1 31 16Zm-6 0a9.007 9.007 0 0 1-2.249 5.95.996.996 0 0 1-1.411.091 1 1 0 0 1-.091-1.411C22.378 19.346 23 17.702 23 16s-.622-3.346-1.751-4.63a1 1 0 0 1 1.502-1.32A9.007 9.007 0 0 1 25 16Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="Use microphone"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M16 22c3.86 0 7-3.141 7-7V8c0-3.859-3.14-7-7-7S9 4.141 9 8v7c0 3.859 3.14 7 7 7ZM11 8c0-2.757 2.243-5 5-5s5 2.243 5 5v7c0 2.757-2.243 5-5 5s-5-2.243-5-5V8Zm5.99 17.95c0 .018.01.032.01.05v2.021h5a1 1 0 1 1 0 2H10.02a1 1 0 1 1 0-2H15V26c0-.018.009-.033.01-.05C9.407 25.447 5 20.731 5 15a1 1 0 1 1 2 0c0 4.963 4.038 9 9 9s9-4.037 9-9a1 1 0 1 1 2 0c0 5.731-4.407 10.447-10.01 10.95Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="pf-v6-c-compass__main">
      <div class="pf-v6-c-compass__main-header">
        <div class="pf-v6-c-panel pf-m-glass">
          <div class="pf-v6-c-panel__main">
            <div class="pf-v6-c-panel__main-body">
              <div class="pf-v6-c-compass__main-header-content">
                <div class="pf-v6-c-compass__main-header-title">
                  <h2 class="pf-v6-c-title pf-m-h1">Page title</h2>
                </div>
                <div class="pf-v6-c-compass__main-header-toolbar">
                  <div class="pf-v6-c-action-list">
                    <div class="pf-v6-c-action-list__group">
                      <div class="pf-v6-c-action-list__item">
                        <button
                          class="pf-v6-c-button pf-m-primary"
                          type="button"
                        >
                          <span class="pf-v6-c-button__text">Add integration</span>
                        </button>
                      </div>
                      <div class="pf-v6-c-action-list__item">
                        <button
                          class="pf-v6-c-button pf-m-secondary"
                          type="button"
                        >
                          <span class="pf-v6-c-button__text">Test integration</span>
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-compass__content">
        <div class="pf-v6-l-grid pf-m-all-6-col pf-m-gutter">
          <div
            class="pf-v6-c-panel pf-m-glass pf-m-scrollable-auto-height pf-m-scrollable"
          >
            <div class="pf-v6-c-panel__main">
              <div class="pf-v6-c-panel__main-body">
                <div class="pf-v6-l-flex pf-m-column pf-m-gap-md">
                  <div
                    class="pf-v6-c-toolbar"
                    id="compass-multiple-sections-toolbar"
                  >
                    <div class="pf-v6-c-toolbar__content">
                      <div class="pf-v6-c-toolbar__content-section pf-m-nowrap">
                        <div
                          class="pf-v6-c-toolbar__group pf-m-show-on-xl pf-m-toggle-group"
                        >
                          <div class="pf-v6-c-toolbar__toggle">
                            <button
                              class="pf-v6-c-menu-toggle pf-m-plain"
                              type="button"
                              aria-expanded="false"
                              aria-label="Show filters"
                              aria-controls="compass-multiple-sections-toolbar-expandable-content"
                            >
                              <span class="pf-v6-c-menu-toggle__icon">
                                <svg
                                  class="pf-v6-svg"
                                  viewBox="0 0 32 32"
                                  fill="currentColor"
                                  aria-hidden="true"
                                  role="img"
                                  width="1em"
                                  height="1em"
                                >
                                  <path
                                    d="M29.875 3.5V7a.876.876 0 0 1-.256.619l-9.744 9.744v10.638a.875.875 0 0 1-.599.83l-6 2a.876.876 0 0 1-.788-.12.874.874 0 0 1-.363-.71V17.363L2.381 7.619A.876.876 0 0 1 2.125 7V3.5c0-.758.617-1.375 1.375-1.375h25c.758 0 1.375.617 1.375 1.375Z"
                                  />
                                </svg>
                              </span>
                            </button>
                          </div>
                          <div class="pf-v6-c-toolbar__item pf-m-bulk-select">
                            <div
                              class="pf-v6-c-menu-toggle pf-m-split-button"
                              id="compass-multiple-sections-toolbar-check"
                            >
                              <label
                                class="pf-v6-c-check pf-m-standalone"
                                for="compass-multiple-sections-toolbar-check-check-input"
                              >
                                <input
                                  class="pf-v6-c-check__input"
                                  type="checkbox"
                                  id="compass-multiple-sections-toolbar-check-check-input"
                                  name="compass-multiple-sections-toolbar-check-check-input"
                                  aria-label="Standalone check"
                                />
                              </label>
                              <button
                                class="pf-v6-c-menu-toggle__button"
                                type="button"
                                aria-expanded="false"
                                id="compass-multiple-sections-toolbar-menu-toggle-toggle-button"
                                aria-label="Menu toggle"
                              >
                                <span class="pf-v6-c-menu-toggle__controls">
                                  <span
                                    class="pf-v6-c-menu-toggle__toggle-icon"
                                  >
                                    <svg
                                      class="pf-v6-svg"
                                      viewBox="0 0 20 20"
                                      fill="currentColor"
                                      aria-hidden="true"
                                      role="img"
                                      width="1em"
                                      height="1em"
                                    >
                                      <path
                                        d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
                                      />
                                    </svg>
                                  </span>
                                </span>
                              </button>
                            </div>
                          </div>

                          <div class="pf-v6-c-toolbar__item">
                            <button
                              class="pf-v6-c-menu-toggle"
                              type="button"
                              aria-expanded="false"
                              id="compass-multiple-sections-toolbar-select-checkbox-status"
                            >
                              <span class="pf-v6-c-menu-toggle__text">Status</span>
                              <span class="pf-v6-c-menu-toggle__controls">
                                <span class="pf-v6-c-menu-toggle__toggle-icon">
                                  <svg
                                    class="pf-v6-svg"
                                    viewBox="0 0 20 20"
                                    fill="currentColor"
                                    aria-hidden="true"
                                    role="img"
                                    width="1em"
                                    height="1em"
                                  >
                                    <path
                                      d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
                                    />
                                  </svg>
                                </span>
                              </span>
                            </button>
                          </div>
                        </div>

                        <div
                          class="pf-v6-c-overflow-menu"
                          id="compass-multiple-sections-toolbar-overflow-menu"
                        >
                          <div
                            class="pf-v6-c-overflow-menu__content pf-v6-u-display-none pf-v6-u-display-flex-on-lg"
                          >
                            <div
                              class="pf-v6-c-overflow-menu__group pf-m-button-group"
                            >
                              <div class="pf-v6-c-overflow-menu__item">
                                <button
                                  class="pf-v6-c-button pf-m-primary"
                                  type="button"
                                >
                                  <span
                                    class="pf-v6-c-button__text"
                                  >Create instance</span>
                                </button>
                              </div>
                            </div>
                          </div>
                          <div class="pf-v6-c-overflow-menu__control">
                            <button
                              class="pf-v6-c-menu-toggle pf-m-plain"
                              type="button"
                              aria-expanded="false"
                              aria-label="Menu toggle"
                              id="compass-multiple-sections-toolbar-overflow-menu-toggle"
                            >
                              <span class="pf-v6-c-menu-toggle__icon">
                                <svg
                                  class="pf-v6-svg"
                                  viewBox="0 0 32 32"
                                  fill="currentColor"
                                  aria-hidden="true"
                                  role="img"
                                  width="1em"
                                  height="1em"
                                >
                                  <path
                                    d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                  />
                                </svg>
                              </span>
                            </button>
                          </div>
                        </div>

                        <div class="pf-v6-c-toolbar__item pf-m-pagination">
                          <div class="pf-v6-c-pagination pf-m-compact">
                            <div class="pf-v6-c-pagination__page-menu">
                              <button
                                class="pf-v6-c-menu-toggle pf-m-text pf-m-plain"
                                type="button"
                                aria-expanded="false"
                                id="compass-multiple-sections-toolbar-top-pagination"
                              >
                                <span class="pf-v6-c-menu-toggle__text">
                                  <b>1 - 10</b>&nbsp;of&nbsp;
                                  <b>36</b>
                                </span>
                                <span class="pf-v6-c-menu-toggle__controls">
                                  <span
                                    class="pf-v6-c-menu-toggle__toggle-icon"
                                  >
                                    <svg
                                      class="pf-v6-svg"
                                      viewBox="0 0 20 20"
                                      fill="currentColor"
                                      aria-hidden="true"
                                      role="img"
                                      width="1em"
                                      height="1em"
                                    >
                                      <path
                                        d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
                                      />
                                    </svg>
                                  </span>
                                </span>
                              </button>
                            </div>
                            <nav
                              class="pf-v6-c-pagination__nav"
                              aria-label="Toolbar top pagination"
                            >
                              <div
                                class="pf-v6-c-pagination__nav-control pf-m-prev"
                              >
                                <button
                                  class="pf-v6-c-button pf-m-plain"
                                  type="button"
                                  disabled
                                  aria-label="Go to previous page"
                                >
                                  <span class="pf-v6-c-button__icon">
                                    <svg
                                      class="pf-v6-svg"
                                      viewBox="0 0 256 512"
                                      fill="currentColor"
                                      aria-hidden="true"
                                      role="img"
                                      width="1em"
                                      height="1em"
                                    >
                                      <path
                                        d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
                                      />
                                    </svg>
                                  </span>
                                </button>
                              </div>
                              <div
                                class="pf-v6-c-pagination__nav-control pf-m-next"
                              >
                                <button
                                  class="pf-v6-c-button pf-m-plain"
                                  type="button"
                                  aria-label="Go to next page"
                                >
                                  <span class="pf-v6-c-button__icon">
                                    <svg
                                      class="pf-v6-svg"
                                      viewBox="0 0 256 512"
                                      fill="currentColor"
                                      aria-hidden="true"
                                      role="img"
                                      width="1em"
                                      height="1em"
                                    >
                                      <path
                                        d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
                                      />
                                    </svg>
                                  </span>
                                </button>
                              </div>
                            </nav>
                          </div>
                        </div>
                      </div>

                      <div
                        class="pf-v6-c-toolbar__expandable-content pf-m-hidden"
                        id="compass-multiple-sections-toolbar-expandable-content"
                        hidden
                      ></div>
                    </div>
                  </div>
                  <div class="pf-v6-l-gallery pf-m-gutter">
                    <div
                      class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                      id="compass-multiple-sections-card-gallery-card-empty-state"
                    >
                      <div class="pf-v6-l-bullseye">
                        <div class="pf-v6-c-empty-state pf-m-xs">
                          <div class="pf-v6-c-empty-state__content">
                            <div class="pf-v6-c-empty-state__icon">
                              <svg
                                class="pf-v6-svg"
                                viewBox="0 0 32 32"
                                fill="currentColor"
                                aria-hidden="true"
                                role="img"
                                width="1em"
                                height="1em"
                              >
                                <path
                                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7 16.125h-5.875V23a1.125 1.125 0 0 1-2.25 0v-5.875H9a1.125 1.125 0 0 1 0-2.25h5.875V9a1.125 1.125 0 0 1 2.25 0v5.875H23a1.125 1.125 0 0 1 0 2.25Z"
                                />
                              </svg>
                            </div>
                            <div class="pf-v6-c-card__title">
                              <h2
                                class="pf-v6-c-card__title-text pf-m-md"
                              >Add a new card to your page</h2>
                            </div>
                            <button
                              class="pf-v6-c-button pf-m-link"
                              type="button"
                            >
                              <span class="pf-v6-c-button__text">Add card</span>
                            </button>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div
                      class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                      id="compass-multiple-sections-card-gallery-card-1"
                    >
                      <div class="pf-v6-c-card__header">
                        <img
                          src="/assets/images/PF-IconLogo.svg"
                          alt="PatternFly logo"
                        />
                        <div class="pf-v6-c-card__actions">
                          <button
                            class="pf-v6-c-menu-toggle pf-m-plain"
                            type="button"
                            aria-expanded="false"
                            aria-label="Menu toggle"
                            id="compass-multiple-sections-card-gallery-card-1-toggle"
                          >
                            <span class="pf-v6-c-menu-toggle__icon">
                              <svg
                                class="pf-v6-svg"
                                viewBox="0 0 32 32"
                                fill="currentColor"
                                aria-hidden="true"
                                role="img"
                                width="1em"
                                height="1em"
                              >
                                <path
                                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                />
                              </svg>
                            </span>
                          </button>
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              id="compass-multiple-sections-card-gallery-card-1-check"
                              name="compass-multiple-sections-card-gallery-card-1-check"
                              aria-labelledby="compass-multiple-sections-card-gallery-card-1-check-label"
                            />
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-c-card__title">
                        <h2
                          class="pf-v6-c-card__title-text"
                          id="compass-multiple-sections-card-gallery-card-1-check-label"
                        >Patternfly</h2>
                        <div class="pf-v6-c-content">
                          <small>Provided by Red Hat</small>
                        </div>
                      </div>
                      <div
                        class="pf-v6-c-card__body"
                      >PatternFly is a community project that promotes design commonality and improves user experience.</div>
                    </div>
                    <div
                      class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                      id="compass-multiple-sections-card-gallery-card-2"
                    >
                      <div class="pf-v6-c-card__header">
                        <img
                          src="/assets/images/activemq-core_200x150.png"
                          width="60px"
                          alt="Logo"
                        />
                        <div class="pf-v6-c-card__actions">
                          <button
                            class="pf-v6-c-menu-toggle pf-m-plain"
                            type="button"
                            aria-expanded="false"
                            aria-label="Menu toggle"
                            id="compass-multiple-sections-card-gallery-card-2-toggle"
                          >
                            <span class="pf-v6-c-menu-toggle__icon">
                              <svg
                                class="pf-v6-svg"
                                viewBox="0 0 32 32"
                                fill="currentColor"
                                aria-hidden="true"
                                role="img"
                                width="1em"
                                height="1em"
                              >
                                <path
                                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                />
                              </svg>
                            </span>
                          </button>
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              id="compass-multiple-sections-card-gallery-card-2-check"
                              name="compass-multiple-sections-card-gallery-card-2-check"
                              aria-labelledby="compass-multiple-sections-card-gallery-card-2-check-label"
                            />
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-c-card__title">
                        <h2
                          class="pf-v6-c-card__title-text"
                          id="compass-multiple-sections-card-gallery-card-2-check-label"
                        >ActiveMq</h2>
                        <div class="pf-v6-c-content">
                          <small>Provided by Red Hat</small>
                        </div>
                      </div>
                      <div
                        class="pf-v6-c-card__body"
                      >The ActiveMQ component allows messages to be sent to a JMS Queue or Topic; or messages to be consumed from a JMS Queue or Topic using Apache ActiveMQ.</div>
                    </div>
                    <div
                      class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                      id="compass-multiple-sections-card-gallery-card-3"
                    >
                      <div class="pf-v6-c-card__header">
                        <img
                          src="/assets/images/camel-spark_200x150.png"
                          width="60px"
                          alt="Logo"
                        />
                        <div class="pf-v6-c-card__actions">
                          <button
                            class="pf-v6-c-menu-toggle pf-m-plain"
                            type="button"
                            aria-expanded="false"
                            aria-label="Menu toggle"
                            id="compass-multiple-sections-card-gallery-card-3-toggle"
                          >
                            <span class="pf-v6-c-menu-toggle__icon">
                              <svg
                                class="pf-v6-svg"
                                viewBox="0 0 32 32"
                                fill="currentColor"
                                aria-hidden="true"
                                role="img"
                                width="1em"
                                height="1em"
                              >
                                <path
                                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                />
                              </svg>
                            </span>
                          </button>
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              id="compass-multiple-sections-card-gallery-card-3-check"
                              name="compass-multiple-sections-card-gallery-card-3-check"
                              aria-labelledby="compass-multiple-sections-card-gallery-card-3-check-label"
                            />
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-c-card__title">
                        <h2
                          class="pf-v6-c-card__title-text"
                          id="compass-multiple-sections-card-gallery-card-3-check-label"
                        >Apache Spark</h2>
                        <div class="pf-v6-c-content">
                          <small>Provided by Red Hat</small>
                        </div>
                      </div>
                      <div
                        class="pf-v6-c-card__body"
                      >This documentation page covers the Apache Spark component for the Apache Camel.</div>
                    </div>
                    <div
                      class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                      id="compass-multiple-sections-card-gallery-card-4"
                    >
                      <div class="pf-v6-c-card__header">
                        <img
                          src="/assets/images/camel-avro_200x150.png"
                          width="60px"
                          alt="Logo"
                        />
                        <div class="pf-v6-c-card__actions">
                          <button
                            class="pf-v6-c-menu-toggle pf-m-plain"
                            type="button"
                            aria-expanded="false"
                            aria-label="Menu toggle"
                            id="compass-multiple-sections-card-gallery-card-4-toggle"
                          >
                            <span class="pf-v6-c-menu-toggle__icon">
                              <svg
                                class="pf-v6-svg"
                                viewBox="0 0 32 32"
                                fill="currentColor"
                                aria-hidden="true"
                                role="img"
                                width="1em"
                                height="1em"
                              >
                                <path
                                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                />
                              </svg>
                            </span>
                          </button>
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              id="compass-multiple-sections-card-gallery-card-4-check"
                              name="compass-multiple-sections-card-gallery-card-4-check"
                              aria-labelledby="compass-multiple-sections-card-gallery-card-4-check-label"
                            />
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-c-card__title">
                        <h2
                          class="pf-v6-c-card__title-text"
                          id="compass-multiple-sections-card-gallery-card-4-check-label"
                        >Avro</h2>
                        <div class="pf-v6-c-content">
                          <small>Provided by Red Hat</small>
                        </div>
                      </div>
                      <div
                        class="pf-v6-c-card__body"
                      >This component provides a dataformat for avro, which allows serialization and deserialization of messages using Apache Avro’s binary dataformat. Moreover, it provides support for Apache Avro’s rpc, by providing producers and consumers endpoint for using avro over netty or http.</div>
                    </div>
                    <div
                      class="pf-v6-c-card pf-m-selectable-raised pf-m-selected-raised pf-m-compact"
                      id="compass-multiple-sections-card-gallery-card-5"
                    >
                      <div class="pf-v6-c-card__header">
                        <img
                          src="/assets/images/FuseConnector_Icons_AzureServices.png"
                          width="60px"
                          alt="Logo"
                        />
                        <div class="pf-v6-c-card__actions">
                          <button
                            class="pf-v6-c-menu-toggle pf-m-plain"
                            type="button"
                            aria-expanded="false"
                            aria-label="Menu toggle"
                            id="compass-multiple-sections-card-gallery-card-5-toggle"
                          >
                            <span class="pf-v6-c-menu-toggle__icon">
                              <svg
                                class="pf-v6-svg"
                                viewBox="0 0 32 32"
                                fill="currentColor"
                                aria-hidden="true"
                                role="img"
                                width="1em"
                                height="1em"
                              >
                                <path
                                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                />
                              </svg>
                            </span>
                          </button>
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              id="compass-multiple-sections-card-gallery-card-5-check"
                              name="compass-multiple-sections-card-gallery-card-5-check"
                              aria-labelledby="compass-multiple-sections-card-gallery-card-5-check-label"
                            />
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-c-card__title">
                        <h2
                          class="pf-v6-c-card__title-text"
                          id="compass-multiple-sections-card-gallery-card-5-check-label"
                        >Azure Services</h2>
                        <div class="pf-v6-c-content">
                          <small>Provided by Red Hat</small>
                        </div>
                      </div>
                      <div
                        class="pf-v6-c-card__body"
                      >The Camel Components for Windows Azure Services provide connectivity to Azure services from Camel.</div>
                    </div>
                    <div
                      class="pf-v6-c-card pf-m-non-selectable-raised pf-m-compact"
                      id="compass-multiple-sections-card-gallery-card-6"
                    >
                      <div class="pf-v6-c-card__header">
                        <img
                          src="/assets/images/camel-saxon_200x150.png"
                          width="60px"
                          alt="Logo"
                        />
                        <div class="pf-v6-c-card__actions">
                          <button
                            class="pf-v6-c-menu-toggle pf-m-plain"
                            type="button"
                            aria-expanded="false"
                            aria-label="Menu toggle"
                            id="compass-multiple-sections-card-gallery-card-6-toggle"
                          >
                            <span class="pf-v6-c-menu-toggle__icon">
                              <svg
                                class="pf-v6-svg"
                                viewBox="0 0 32 32"
                                fill="currentColor"
                                aria-hidden="true"
                                role="img"
                                width="1em"
                                height="1em"
                              >
                                <path
                                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                />
                              </svg>
                            </span>
                          </button>
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              id="compass-multiple-sections-card-gallery-card-6-check"
                              name="compass-multiple-sections-card-gallery-card-6-check"
                              disabled
                              aria-labelledby="compass-multiple-sections-card-gallery-card-6-check-label"
                            />
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-c-card__title">
                        <h2
                          class="pf-v6-c-card__title-text"
                          id="compass-multiple-sections-card-gallery-card-6-check-label"
                        >Crypto</h2>
                        <div class="pf-v6-c-content">
                          <small>Provided by Red Hat</small>
                        </div>
                      </div>
                      <div
                        class="pf-v6-c-card__body"
                      >For providing flexible endpoints to sign and verify exchanges using the Signature Service of the Java Cryptographic Extension.</div>
                    </div>
                    <div
                      class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                      id="compass-multiple-sections-card-gallery-card-7"
                    >
                      <div class="pf-v6-c-card__header">
                        <img
                          src="/assets/images/camel-dropbox_200x150.png"
                          width="60px"
                          alt="Logo"
                        />
                        <div class="pf-v6-c-card__actions">
                          <button
                            class="pf-v6-c-menu-toggle pf-m-plain"
                            type="button"
                            aria-expanded="false"
                            aria-label="Menu toggle"
                            id="compass-multiple-sections-card-gallery-card-7-toggle"
                          >
                            <span class="pf-v6-c-menu-toggle__icon">
                              <svg
                                class="pf-v6-svg"
                                viewBox="0 0 32 32"
                                fill="currentColor"
                                aria-hidden="true"
                                role="img"
                                width="1em"
                                height="1em"
                              >
                                <path
                                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                />
                              </svg>
                            </span>
                          </button>
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              id="compass-multiple-sections-card-gallery-card-7-check"
                              name="compass-multiple-sections-card-gallery-card-7-check"
                              aria-labelledby="compass-multiple-sections-card-gallery-card-7-check-label"
                            />
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-c-card__title">
                        <h2
                          class="pf-v6-c-card__title-text"
                          id="compass-multiple-sections-card-gallery-card-7-check-label"
                        >DropBox</h2>
                        <div class="pf-v6-c-content">
                          <small>Provided by Red Hat</small>
                        </div>
                      </div>
                      <div
                        class="pf-v6-c-card__body"
                      >The dropbox: component allows you to treat Dropbox remote folders as a producer or consumer of messages.</div>
                    </div>
                    <div
                      class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                      id="compass-multiple-sections-card-gallery-card-8"
                    >
                      <div class="pf-v6-c-card__header">
                        <img
                          src="/assets/images/camel-infinispan_200x150.png"
                          width="60px"
                          alt="Logo"
                        />
                        <div class="pf-v6-c-card__actions">
                          <button
                            class="pf-v6-c-menu-toggle pf-m-plain"
                            type="button"
                            aria-expanded="false"
                            aria-label="Menu toggle"
                            id="compass-multiple-sections-card-gallery-card-8-toggle"
                          >
                            <span class="pf-v6-c-menu-toggle__icon">
                              <svg
                                class="pf-v6-svg"
                                viewBox="0 0 32 32"
                                fill="currentColor"
                                aria-hidden="true"
                                role="img"
                                width="1em"
                                height="1em"
                              >
                                <path
                                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                />
                              </svg>
                            </span>
                          </button>
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              id="compass-multiple-sections-card-gallery-card-8-check"
                              name="compass-multiple-sections-card-gallery-card-8-check"
                              aria-labelledby="compass-multiple-sections-card-gallery-card-8-check-label"
                            />
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-c-card__title">
                        <h2
                          class="pf-v6-c-card__title-text"
                          id="compass-multiple-sections-card-gallery-card-8-check-label"
                        >JBoss Data Grid</h2>
                        <div class="pf-v6-c-content">
                          <small>Provided by Red Hat</small>
                        </div>
                      </div>
                      <div
                        class="pf-v6-c-card__body"
                      >Read or write to a fully-supported distributed cache and data grid for faster integration services.</div>
                    </div>
                    <div
                      class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                      id="compass-multiple-sections-card-gallery-card-9"
                    >
                      <div class="pf-v6-c-card__header">
                        <img
                          src="/assets/images/FuseConnector_Icons_REST.png"
                          width="60px"
                          alt="Logo"
                        />
                        <div class="pf-v6-c-card__actions">
                          <button
                            class="pf-v6-c-menu-toggle pf-m-plain"
                            type="button"
                            aria-expanded="false"
                            aria-label="Menu toggle"
                            id="compass-multiple-sections-card-gallery-card-9-toggle"
                          >
                            <span class="pf-v6-c-menu-toggle__icon">
                              <svg
                                class="pf-v6-svg"
                                viewBox="0 0 32 32"
                                fill="currentColor"
                                aria-hidden="true"
                                role="img"
                                width="1em"
                                height="1em"
                              >
                                <path
                                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                />
                              </svg>
                            </span>
                          </button>
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              id="compass-multiple-sections-card-gallery-card-9-check"
                              name="compass-multiple-sections-card-gallery-card-9-check"
                              aria-labelledby="compass-multiple-sections-card-gallery-card-9-check-label"
                            />
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-c-card__title">
                        <h2
                          class="pf-v6-c-card__title-text"
                          id="compass-multiple-sections-card-gallery-card-9-check-label"
                        >Rest</h2>
                        <div class="pf-v6-c-content">
                          <small>Provided by Red Hat</small>
                        </div>
                      </div>
                      <div class="pf-v6-c-card__body">
                        The rest component allows to define REST endpoints (consumer) using the Rest DSL and plugin to other Camel components as the REST transport.
                        From Camel 2.18 onwards the rest component can also be used as a client (producer) to call REST services.
                      </div>
                    </div>
                    <div
                      class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                      id="compass-multiple-sections-card-gallery-card-10"
                    >
                      <div class="pf-v6-c-card__header">
                        <img
                          src="/assets/images/camel-swagger-java_200x150.png"
                          width="60px"
                          alt="Logo"
                        />
                        <div class="pf-v6-c-card__actions">
                          <button
                            class="pf-v6-c-menu-toggle pf-m-plain"
                            type="button"
                            aria-expanded="false"
                            aria-label="Menu toggle"
                            id="compass-multiple-sections-card-gallery-card-10-toggle"
                          >
                            <span class="pf-v6-c-menu-toggle__icon">
                              <svg
                                class="pf-v6-svg"
                                viewBox="0 0 32 32"
                                fill="currentColor"
                                aria-hidden="true"
                                role="img"
                                width="1em"
                                height="1em"
                              >
                                <path
                                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                />
                              </svg>
                            </span>
                          </button>
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              id="compass-multiple-sections-card-gallery-card-10-check"
                              name="compass-multiple-sections-card-gallery-card-10-check"
                              aria-labelledby="compass-multiple-sections-card-gallery-card-10-check-label"
                            />
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-c-card__title">
                        <h2
                          class="pf-v6-c-card__title-text"
                          id="compass-multiple-sections-card-gallery-card-10-check-label"
                        >SWAGGER</h2>
                        <div class="pf-v6-c-content">
                          <small>Provided by Red Hat</small>
                        </div>
                      </div>
                      <div
                        class="pf-v6-c-card__body"
                      >Expose REST services and their APIs using Swagger specification.</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div
            class="pf-v6-c-panel pf-m-glass pf-m-scrollable-auto-height pf-m-scrollable"
          >
            <div class="pf-v6-c-panel__main">
              <div class="pf-v6-c-panel__main-body">
                <div class="pf-v6-l-flex pf-m-column pf-m-gap-md">
                  <div
                    class="pf-v6-c-toolbar"
                    id="compass-multiple-sections-toolbar-2"
                  >
                    <div class="pf-v6-c-toolbar__content">
                      <div class="pf-v6-c-toolbar__content-section pf-m-nowrap">
                        <div
                          class="pf-v6-c-toolbar__group pf-m-show-on-xl pf-m-toggle-group"
                        >
                          <div class="pf-v6-c-toolbar__toggle">
                            <button
                              class="pf-v6-c-menu-toggle pf-m-plain"
                              type="button"
                              aria-expanded="false"
                              aria-label="Show filters"
                              aria-controls="compass-multiple-sections-toolbar-2-expandable-content"
                            >
                              <span class="pf-v6-c-menu-toggle__icon">
                                <svg
                                  class="pf-v6-svg"
                                  viewBox="0 0 32 32"
                                  fill="currentColor"
                                  aria-hidden="true"
                                  role="img"
                                  width="1em"
                                  height="1em"
                                >
                                  <path
                                    d="M29.875 3.5V7a.876.876 0 0 1-.256.619l-9.744 9.744v10.638a.875.875 0 0 1-.599.83l-6 2a.876.876 0 0 1-.788-.12.874.874 0 0 1-.363-.71V17.363L2.381 7.619A.876.876 0 0 1 2.125 7V3.5c0-.758.617-1.375 1.375-1.375h25c.758 0 1.375.617 1.375 1.375Z"
                                  />
                                </svg>
                              </span>
                            </button>
                          </div>
                          <div class="pf-v6-c-toolbar__item pf-m-bulk-select">
                            <div
                              class="pf-v6-c-menu-toggle pf-m-split-button"
                              id="compass-multiple-sections-toolbar-2-check"
                            >
                              <label
                                class="pf-v6-c-check pf-m-standalone"
                                for="compass-multiple-sections-toolbar-2-check-check-input"
                              >
                                <input
                                  class="pf-v6-c-check__input"
                                  type="checkbox"
                                  id="compass-multiple-sections-toolbar-2-check-check-input"
                                  name="compass-multiple-sections-toolbar-2-check-check-input"
                                  aria-label="Standalone check"
                                />
                              </label>
                              <button
                                class="pf-v6-c-menu-toggle__button"
                                type="button"
                                aria-expanded="false"
                                id="compass-multiple-sections-toolbar-2-menu-toggle-toggle-button"
                                aria-label="Menu toggle"
                              >
                                <span class="pf-v6-c-menu-toggle__controls">
                                  <span
                                    class="pf-v6-c-menu-toggle__toggle-icon"
                                  >
                                    <svg
                                      class="pf-v6-svg"
                                      viewBox="0 0 20 20"
                                      fill="currentColor"
                                      aria-hidden="true"
                                      role="img"
                                      width="1em"
                                      height="1em"
                                    >
                                      <path
                                        d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
                                      />
                                    </svg>
                                  </span>
                                </span>
                              </button>
                            </div>
                          </div>

                          <div class="pf-v6-c-toolbar__item">
                            <button
                              class="pf-v6-c-menu-toggle"
                              type="button"
                              aria-expanded="false"
                              id="compass-multiple-sections-toolbar-2-select-checkbox-status"
                            >
                              <span class="pf-v6-c-menu-toggle__text">Status</span>
                              <span class="pf-v6-c-menu-toggle__controls">
                                <span class="pf-v6-c-menu-toggle__toggle-icon">
                                  <svg
                                    class="pf-v6-svg"
                                    viewBox="0 0 20 20"
                                    fill="currentColor"
                                    aria-hidden="true"
                                    role="img"
                                    width="1em"
                                    height="1em"
                                  >
                                    <path
                                      d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
                                    />
                                  </svg>
                                </span>
                              </span>
                            </button>
                          </div>
                        </div>

                        <div
                          class="pf-v6-c-overflow-menu"
                          id="compass-multiple-sections-toolbar-2-overflow-menu"
                        >
                          <div
                            class="pf-v6-c-overflow-menu__content pf-v6-u-display-none pf-v6-u-display-flex-on-lg"
                          >
                            <div
                              class="pf-v6-c-overflow-menu__group pf-m-button-group"
                            >
                              <div class="pf-v6-c-overflow-menu__item">
                                <button
                                  class="pf-v6-c-button pf-m-primary"
                                  type="button"
                                >
                                  <span
                                    class="pf-v6-c-button__text"
                                  >Create instance</span>
                                </button>
                              </div>
                            </div>
                          </div>
                          <div class="pf-v6-c-overflow-menu__control">
                            <button
                              class="pf-v6-c-menu-toggle pf-m-plain"
                              type="button"
                              aria-expanded="false"
                              aria-label="Menu toggle"
                              id="compass-multiple-sections-toolbar-2-overflow-menu-toggle"
                            >
                              <span class="pf-v6-c-menu-toggle__icon">
                                <svg
                                  class="pf-v6-svg"
                                  viewBox="0 0 32 32"
                                  fill="currentColor"
                                  aria-hidden="true"
                                  role="img"
                                  width="1em"
                                  height="1em"
                                >
                                  <path
                                    d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                  />
                                </svg>
                              </span>
                            </button>
                          </div>
                        </div>

                        <div class="pf-v6-c-toolbar__item pf-m-pagination">
                          <div class="pf-v6-c-pagination pf-m-compact">
                            <div class="pf-v6-c-pagination__page-menu">
                              <button
                                class="pf-v6-c-menu-toggle pf-m-text pf-m-plain"
                                type="button"
                                aria-expanded="false"
                                id="compass-multiple-sections-toolbar-2-top-pagination"
                              >
                                <span class="pf-v6-c-menu-toggle__text">
                                  <b>1 - 10</b>&nbsp;of&nbsp;
                                  <b>36</b>
                                </span>
                                <span class="pf-v6-c-menu-toggle__controls">
                                  <span
                                    class="pf-v6-c-menu-toggle__toggle-icon"
                                  >
                                    <svg
                                      class="pf-v6-svg"
                                      viewBox="0 0 20 20"
                                      fill="currentColor"
                                      aria-hidden="true"
                                      role="img"
                                      width="1em"
                                      height="1em"
                                    >
                                      <path
                                        d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
                                      />
                                    </svg>
                                  </span>
                                </span>
                              </button>
                            </div>
                            <nav
                              class="pf-v6-c-pagination__nav"
                              aria-label="Toolbar top pagination"
                            >
                              <div
                                class="pf-v6-c-pagination__nav-control pf-m-prev"
                              >
                                <button
                                  class="pf-v6-c-button pf-m-plain"
                                  type="button"
                                  disabled
                                  aria-label="Go to previous page"
                                >
                                  <span class="pf-v6-c-button__icon">
                                    <svg
                                      class="pf-v6-svg"
                                      viewBox="0 0 256 512"
                                      fill="currentColor"
                                      aria-hidden="true"
                                      role="img"
                                      width="1em"
                                      height="1em"
                                    >
                                      <path
                                        d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
                                      />
                                    </svg>
                                  </span>
                                </button>
                              </div>
                              <div
                                class="pf-v6-c-pagination__nav-control pf-m-next"
                              >
                                <button
                                  class="pf-v6-c-button pf-m-plain"
                                  type="button"
                                  aria-label="Go to next page"
                                >
                                  <span class="pf-v6-c-button__icon">
                                    <svg
                                      class="pf-v6-svg"
                                      viewBox="0 0 256 512"
                                      fill="currentColor"
                                      aria-hidden="true"
                                      role="img"
                                      width="1em"
                                      height="1em"
                                    >
                                      <path
                                        d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
                                      />
                                    </svg>
                                  </span>
                                </button>
                              </div>
                            </nav>
                          </div>
                        </div>
                      </div>

                      <div
                        class="pf-v6-c-toolbar__expandable-content pf-m-hidden"
                        id="compass-multiple-sections-toolbar-2-expandable-content"
                        hidden
                      ></div>
                    </div>
                  </div>
                  <div class="pf-v6-l-gallery pf-m-gutter">
                    <div
                      class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                      id="compass-multiple-sections-card-gallery-2-card-empty-state"
                    >
                      <div class="pf-v6-l-bullseye">
                        <div class="pf-v6-c-empty-state pf-m-xs">
                          <div class="pf-v6-c-empty-state__content">
                            <div class="pf-v6-c-empty-state__icon">
                              <svg
                                class="pf-v6-svg"
                                viewBox="0 0 32 32"
                                fill="currentColor"
                                aria-hidden="true"
                                role="img"
                                width="1em"
                                height="1em"
                              >
                                <path
                                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7 16.125h-5.875V23a1.125 1.125 0 0 1-2.25 0v-5.875H9a1.125 1.125 0 0 1 0-2.25h5.875V9a1.125 1.125 0 0 1 2.25 0v5.875H23a1.125 1.125 0 0 1 0 2.25Z"
                                />
                              </svg>
                            </div>
                            <div class="pf-v6-c-card__title">
                              <h2
                                class="pf-v6-c-card__title-text pf-m-md"
                              >Add a new card to your page</h2>
                            </div>
                            <button
                              class="pf-v6-c-button pf-m-link"
                              type="button"
                            >
                              <span class="pf-v6-c-button__text">Add card</span>
                            </button>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div
                      class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                      id="compass-multiple-sections-card-gallery-2-card-1"
                    >
                      <div class="pf-v6-c-card__header">
                        <img
                          src="/assets/images/PF-IconLogo.svg"
                          alt="PatternFly logo"
                        />
                        <div class="pf-v6-c-card__actions">
                          <button
                            class="pf-v6-c-menu-toggle pf-m-plain"
                            type="button"
                            aria-expanded="false"
                            aria-label="Menu toggle"
                            id="compass-multiple-sections-card-gallery-2-card-1-toggle"
                          >
                            <span class="pf-v6-c-menu-toggle__icon">
                              <svg
                                class="pf-v6-svg"
                                viewBox="0 0 32 32"
                                fill="currentColor"
                                aria-hidden="true"
                                role="img"
                                width="1em"
                                height="1em"
                              >
                                <path
                                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                />
                              </svg>
                            </span>
                          </button>
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              id="compass-multiple-sections-card-gallery-2-card-1-check"
                              name="compass-multiple-sections-card-gallery-2-card-1-check"
                              aria-labelledby="compass-multiple-sections-card-gallery-2-card-1-check-label"
                            />
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-c-card__title">
                        <h2
                          class="pf-v6-c-card__title-text"
                          id="compass-multiple-sections-card-gallery-2-card-1-check-label"
                        >Patternfly</h2>
                        <div class="pf-v6-c-content">
                          <small>Provided by Red Hat</small>
                        </div>
                      </div>
                      <div
                        class="pf-v6-c-card__body"
                      >PatternFly is a community project that promotes design commonality and improves user experience.</div>
                    </div>
                    <div
                      class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                      id="compass-multiple-sections-card-gallery-2-card-2"
                    >
                      <div class="pf-v6-c-card__header">
                        <img
                          src="/assets/images/activemq-core_200x150.png"
                          width="60px"
                          alt="Logo"
                        />
                        <div class="pf-v6-c-card__actions">
                          <button
                            class="pf-v6-c-menu-toggle pf-m-plain"
                            type="button"
                            aria-expanded="false"
                            aria-label="Menu toggle"
                            id="compass-multiple-sections-card-gallery-2-card-2-toggle"
                          >
                            <span class="pf-v6-c-menu-toggle__icon">
                              <svg
                                class="pf-v6-svg"
                                viewBox="0 0 32 32"
                                fill="currentColor"
                                aria-hidden="true"
                                role="img"
                                width="1em"
                                height="1em"
                              >
                                <path
                                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                />
                              </svg>
                            </span>
                          </button>
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              id="compass-multiple-sections-card-gallery-2-card-2-check"
                              name="compass-multiple-sections-card-gallery-2-card-2-check"
                              aria-labelledby="compass-multiple-sections-card-gallery-2-card-2-check-label"
                            />
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-c-card__title">
                        <h2
                          class="pf-v6-c-card__title-text"
                          id="compass-multiple-sections-card-gallery-2-card-2-check-label"
                        >ActiveMq</h2>
                        <div class="pf-v6-c-content">
                          <small>Provided by Red Hat</small>
                        </div>
                      </div>
                      <div
                        class="pf-v6-c-card__body"
                      >The ActiveMQ component allows messages to be sent to a JMS Queue or Topic; or messages to be consumed from a JMS Queue or Topic using Apache ActiveMQ.</div>
                    </div>
                    <div
                      class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                      id="compass-multiple-sections-card-gallery-2-card-3"
                    >
                      <div class="pf-v6-c-card__header">
                        <img
                          src="/assets/images/camel-spark_200x150.png"
                          width="60px"
                          alt="Logo"
                        />
                        <div class="pf-v6-c-card__actions">
                          <button
                            class="pf-v6-c-menu-toggle pf-m-plain"
                            type="button"
                            aria-expanded="false"
                            aria-label="Menu toggle"
                            id="compass-multiple-sections-card-gallery-2-card-3-toggle"
                          >
                            <span class="pf-v6-c-menu-toggle__icon">
                              <svg
                                class="pf-v6-svg"
                                viewBox="0 0 32 32"
                                fill="currentColor"
                                aria-hidden="true"
                                role="img"
                                width="1em"
                                height="1em"
                              >
                                <path
                                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                />
                              </svg>
                            </span>
                          </button>
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              id="compass-multiple-sections-card-gallery-2-card-3-check"
                              name="compass-multiple-sections-card-gallery-2-card-3-check"
                              aria-labelledby="compass-multiple-sections-card-gallery-2-card-3-check-label"
                            />
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-c-card__title">
                        <h2
                          class="pf-v6-c-card__title-text"
                          id="compass-multiple-sections-card-gallery-2-card-3-check-label"
                        >Apache Spark</h2>
                        <div class="pf-v6-c-content">
                          <small>Provided by Red Hat</small>
                        </div>
                      </div>
                      <div
                        class="pf-v6-c-card__body"
                      >This documentation page covers the Apache Spark component for the Apache Camel.</div>
                    </div>
                    <div
                      class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                      id="compass-multiple-sections-card-gallery-2-card-4"
                    >
                      <div class="pf-v6-c-card__header">
                        <img
                          src="/assets/images/camel-avro_200x150.png"
                          width="60px"
                          alt="Logo"
                        />
                        <div class="pf-v6-c-card__actions">
                          <button
                            class="pf-v6-c-menu-toggle pf-m-plain"
                            type="button"
                            aria-expanded="false"
                            aria-label="Menu toggle"
                            id="compass-multiple-sections-card-gallery-2-card-4-toggle"
                          >
                            <span class="pf-v6-c-menu-toggle__icon">
                              <svg
                                class="pf-v6-svg"
                                viewBox="0 0 32 32"
                                fill="currentColor"
                                aria-hidden="true"
                                role="img"
                                width="1em"
                                height="1em"
                              >
                                <path
                                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                />
                              </svg>
                            </span>
                          </button>
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              id="compass-multiple-sections-card-gallery-2-card-4-check"
                              name="compass-multiple-sections-card-gallery-2-card-4-check"
                              aria-labelledby="compass-multiple-sections-card-gallery-2-card-4-check-label"
                            />
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-c-card__title">
                        <h2
                          class="pf-v6-c-card__title-text"
                          id="compass-multiple-sections-card-gallery-2-card-4-check-label"
                        >Avro</h2>
                        <div class="pf-v6-c-content">
                          <small>Provided by Red Hat</small>
                        </div>
                      </div>
                      <div
                        class="pf-v6-c-card__body"
                      >This component provides a dataformat for avro, which allows serialization and deserialization of messages using Apache Avro’s binary dataformat. Moreover, it provides support for Apache Avro’s rpc, by providing producers and consumers endpoint for using avro over netty or http.</div>
                    </div>
                    <div
                      class="pf-v6-c-card pf-m-selectable-raised pf-m-selected-raised pf-m-compact"
                      id="compass-multiple-sections-card-gallery-2-card-5"
                    >
                      <div class="pf-v6-c-card__header">
                        <img
                          src="/assets/images/FuseConnector_Icons_AzureServices.png"
                          width="60px"
                          alt="Logo"
                        />
                        <div class="pf-v6-c-card__actions">
                          <button
                            class="pf-v6-c-menu-toggle pf-m-plain"
                            type="button"
                            aria-expanded="false"
                            aria-label="Menu toggle"
                            id="compass-multiple-sections-card-gallery-2-card-5-toggle"
                          >
                            <span class="pf-v6-c-menu-toggle__icon">
                              <svg
                                class="pf-v6-svg"
                                viewBox="0 0 32 32"
                                fill="currentColor"
                                aria-hidden="true"
                                role="img"
                                width="1em"
                                height="1em"
                              >
                                <path
                                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                />
                              </svg>
                            </span>
                          </button>
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              id="compass-multiple-sections-card-gallery-2-card-5-check"
                              name="compass-multiple-sections-card-gallery-2-card-5-check"
                              aria-labelledby="compass-multiple-sections-card-gallery-2-card-5-check-label"
                            />
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-c-card__title">
                        <h2
                          class="pf-v6-c-card__title-text"
                          id="compass-multiple-sections-card-gallery-2-card-5-check-label"
                        >Azure Services</h2>
                        <div class="pf-v6-c-content">
                          <small>Provided by Red Hat</small>
                        </div>
                      </div>
                      <div
                        class="pf-v6-c-card__body"
                      >The Camel Components for Windows Azure Services provide connectivity to Azure services from Camel.</div>
                    </div>
                    <div
                      class="pf-v6-c-card pf-m-non-selectable-raised pf-m-compact"
                      id="compass-multiple-sections-card-gallery-2-card-6"
                    >
                      <div class="pf-v6-c-card__header">
                        <img
                          src="/assets/images/camel-saxon_200x150.png"
                          width="60px"
                          alt="Logo"
                        />
                        <div class="pf-v6-c-card__actions">
                          <button
                            class="pf-v6-c-menu-toggle pf-m-plain"
                            type="button"
                            aria-expanded="false"
                            aria-label="Menu toggle"
                            id="compass-multiple-sections-card-gallery-2-card-6-toggle"
                          >
                            <span class="pf-v6-c-menu-toggle__icon">
                              <svg
                                class="pf-v6-svg"
                                viewBox="0 0 32 32"
                                fill="currentColor"
                                aria-hidden="true"
                                role="img"
                                width="1em"
                                height="1em"
                              >
                                <path
                                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                />
                              </svg>
                            </span>
                          </button>
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              id="compass-multiple-sections-card-gallery-2-card-6-check"
                              name="compass-multiple-sections-card-gallery-2-card-6-check"
                              disabled
                              aria-labelledby="compass-multiple-sections-card-gallery-2-card-6-check-label"
                            />
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-c-card__title">
                        <h2
                          class="pf-v6-c-card__title-text"
                          id="compass-multiple-sections-card-gallery-2-card-6-check-label"
                        >Crypto</h2>
                        <div class="pf-v6-c-content">
                          <small>Provided by Red Hat</small>
                        </div>
                      </div>
                      <div
                        class="pf-v6-c-card__body"
                      >For providing flexible endpoints to sign and verify exchanges using the Signature Service of the Java Cryptographic Extension.</div>
                    </div>
                    <div
                      class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                      id="compass-multiple-sections-card-gallery-2-card-7"
                    >
                      <div class="pf-v6-c-card__header">
                        <img
                          src="/assets/images/camel-dropbox_200x150.png"
                          width="60px"
                          alt="Logo"
                        />
                        <div class="pf-v6-c-card__actions">
                          <button
                            class="pf-v6-c-menu-toggle pf-m-plain"
                            type="button"
                            aria-expanded="false"
                            aria-label="Menu toggle"
                            id="compass-multiple-sections-card-gallery-2-card-7-toggle"
                          >
                            <span class="pf-v6-c-menu-toggle__icon">
                              <svg
                                class="pf-v6-svg"
                                viewBox="0 0 32 32"
                                fill="currentColor"
                                aria-hidden="true"
                                role="img"
                                width="1em"
                                height="1em"
                              >
                                <path
                                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                />
                              </svg>
                            </span>
                          </button>
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              id="compass-multiple-sections-card-gallery-2-card-7-check"
                              name="compass-multiple-sections-card-gallery-2-card-7-check"
                              aria-labelledby="compass-multiple-sections-card-gallery-2-card-7-check-label"
                            />
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-c-card__title">
                        <h2
                          class="pf-v6-c-card__title-text"
                          id="compass-multiple-sections-card-gallery-2-card-7-check-label"
                        >DropBox</h2>
                        <div class="pf-v6-c-content">
                          <small>Provided by Red Hat</small>
                        </div>
                      </div>
                      <div
                        class="pf-v6-c-card__body"
                      >The dropbox: component allows you to treat Dropbox remote folders as a producer or consumer of messages.</div>
                    </div>
                    <div
                      class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                      id="compass-multiple-sections-card-gallery-2-card-8"
                    >
                      <div class="pf-v6-c-card__header">
                        <img
                          src="/assets/images/camel-infinispan_200x150.png"
                          width="60px"
                          alt="Logo"
                        />
                        <div class="pf-v6-c-card__actions">
                          <button
                            class="pf-v6-c-menu-toggle pf-m-plain"
                            type="button"
                            aria-expanded="false"
                            aria-label="Menu toggle"
                            id="compass-multiple-sections-card-gallery-2-card-8-toggle"
                          >
                            <span class="pf-v6-c-menu-toggle__icon">
                              <svg
                                class="pf-v6-svg"
                                viewBox="0 0 32 32"
                                fill="currentColor"
                                aria-hidden="true"
                                role="img"
                                width="1em"
                                height="1em"
                              >
                                <path
                                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                />
                              </svg>
                            </span>
                          </button>
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              id="compass-multiple-sections-card-gallery-2-card-8-check"
                              name="compass-multiple-sections-card-gallery-2-card-8-check"
                              aria-labelledby="compass-multiple-sections-card-gallery-2-card-8-check-label"
                            />
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-c-card__title">
                        <h2
                          class="pf-v6-c-card__title-text"
                          id="compass-multiple-sections-card-gallery-2-card-8-check-label"
                        >JBoss Data Grid</h2>
                        <div class="pf-v6-c-content">
                          <small>Provided by Red Hat</small>
                        </div>
                      </div>
                      <div
                        class="pf-v6-c-card__body"
                      >Read or write to a fully-supported distributed cache and data grid for faster integration services.</div>
                    </div>
                    <div
                      class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                      id="compass-multiple-sections-card-gallery-2-card-9"
                    >
                      <div class="pf-v6-c-card__header">
                        <img
                          src="/assets/images/FuseConnector_Icons_REST.png"
                          width="60px"
                          alt="Logo"
                        />
                        <div class="pf-v6-c-card__actions">
                          <button
                            class="pf-v6-c-menu-toggle pf-m-plain"
                            type="button"
                            aria-expanded="false"
                            aria-label="Menu toggle"
                            id="compass-multiple-sections-card-gallery-2-card-9-toggle"
                          >
                            <span class="pf-v6-c-menu-toggle__icon">
                              <svg
                                class="pf-v6-svg"
                                viewBox="0 0 32 32"
                                fill="currentColor"
                                aria-hidden="true"
                                role="img"
                                width="1em"
                                height="1em"
                              >
                                <path
                                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                />
                              </svg>
                            </span>
                          </button>
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              id="compass-multiple-sections-card-gallery-2-card-9-check"
                              name="compass-multiple-sections-card-gallery-2-card-9-check"
                              aria-labelledby="compass-multiple-sections-card-gallery-2-card-9-check-label"
                            />
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-c-card__title">
                        <h2
                          class="pf-v6-c-card__title-text"
                          id="compass-multiple-sections-card-gallery-2-card-9-check-label"
                        >Rest</h2>
                        <div class="pf-v6-c-content">
                          <small>Provided by Red Hat</small>
                        </div>
                      </div>
                      <div class="pf-v6-c-card__body">
                        The rest component allows to define REST endpoints (consumer) using the Rest DSL and plugin to other Camel components as the REST transport.
                        From Camel 2.18 onwards the rest component can also be used as a client (producer) to call REST services.
                      </div>
                    </div>
                    <div
                      class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                      id="compass-multiple-sections-card-gallery-2-card-10"
                    >
                      <div class="pf-v6-c-card__header">
                        <img
                          src="/assets/images/camel-swagger-java_200x150.png"
                          width="60px"
                          alt="Logo"
                        />
                        <div class="pf-v6-c-card__actions">
                          <button
                            class="pf-v6-c-menu-toggle pf-m-plain"
                            type="button"
                            aria-expanded="false"
                            aria-label="Menu toggle"
                            id="compass-multiple-sections-card-gallery-2-card-10-toggle"
                          >
                            <span class="pf-v6-c-menu-toggle__icon">
                              <svg
                                class="pf-v6-svg"
                                viewBox="0 0 32 32"
                                fill="currentColor"
                                aria-hidden="true"
                                role="img"
                                width="1em"
                                height="1em"
                              >
                                <path
                                  d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                />
                              </svg>
                            </span>
                          </button>
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              id="compass-multiple-sections-card-gallery-2-card-10-check"
                              name="compass-multiple-sections-card-gallery-2-card-10-check"
                              aria-labelledby="compass-multiple-sections-card-gallery-2-card-10-check-label"
                            />
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-c-card__title">
                        <h2
                          class="pf-v6-c-card__title-text"
                          id="compass-multiple-sections-card-gallery-2-card-10-check-label"
                        >SWAGGER</h2>
                        <div class="pf-v6-c-content">
                          <small>Provided by Red Hat</small>
                        </div>
                      </div>
                      <div
                        class="pf-v6-c-card__body"
                      >Expose REST services and their APIs using Swagger specification.</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-compass__main-footer pf-m-expanded">
        <div class="pf-v6-c-compass__message-bar">
          <div class="pf-v6-c-panel pf-m-pill pf-m-glass pf-m-no-border">
            <div class="pf-v6-c-panel__main">chatbot message bar</div>
          </div>
        </div>
      </div>
    </div>
    <div class="pf-v6-c-compass__sidebar pf-m-expanded pf-m-end">
      <div class="pf-v6-c-panel pf-m-pill pf-m-glass">
        <div class="pf-v6-c-panel__main">
          <div class="pf-v6-c-panel__main-body">
            <div class="pf-v6-c-action-list pf-m-icons pf-m-vertical">
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="Notifications"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M28 21c-1.103 0-2-.897-2-2v-4c0-4.885-3.523-8.955-8.159-9.823.405-.445.659-1.03.659-1.677C18.5 2.122 17.379 1 16 1s-2.5 1.122-2.5 2.5c0 .647.254 1.233.659 1.677C9.523 6.045 6 10.115 6 15v4c0 1.103-.897 2-2 2a1 1 0 0 0-1 1v3.5c0 .827.673 1.5 1.5 1.5H12c0 2.206 1.794 4 4 4s4-1.794 4-4h7.5c.827 0 1.5-.673 1.5-1.5V22a1 1 0 0 0-1-1Zm-1 4H5v-2.126A4.006 4.006 0 0 0 8 19v-4c0-4.411 3.589-8 8-8s8 3.589 8 8v4a4.008 4.008 0 0 0 3 3.874V25Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="List"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M31 16a1 1 0 0 1-1 1H9a1 1 0 0 1 0-2h21a1 1 0 0 1 1 1Zm-1 9H9a1 1 0 0 0 0 2h21a1 1 0 0 0 0-2ZM9 7h21a1 1 0 0 0 0-2H9a1 1 0 0 0 0 2ZM2 4.51a1.5 1.5 0 1 0 .001 3.001A1.5 1.5 0 0 0 2 4.51Zm0 10a1.5 1.5 0 1 0 .001 3.001A1.5 1.5 0 0 0 2 14.51Zm0 10a1.5 1.5 0 1 0 .001 3.001A1.5 1.5 0 0 0 2 24.51Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="Zap"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M15 31a1 1 0 0 1-1-1V19h-4a.999.999 0 0 1-.916-1.401l7-16A1 1 0 0 1 18 2v11h4a.999.999 0 0 1 .916 1.401l-7 16A.998.998 0 0 1 15 31Zm-3.471-14H14.5c.827 0 1.5.673 1.5 1.5v6.719L20.471 15H17.5c-.827 0-1.5-.673-1.5-1.5V6.781L11.529 17Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="Download"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M30 29a1 1 0 0 1-1 1H3a1 1 0 0 1 0-2h26a1 1 0 0 1 1 1Zm-15.061-4.646c.292.292.676.438 1.061.438s.768-.146 1.061-.438l8.646-8.646a.999.999 0 1 0-1.414-1.414L17 21.587V3a1 1 0 0 0-2 0v18.586l-7.293-7.293a.999.999 0 1 0-1.414 1.414l8.646 8.646Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
              <div class="pf-v6-c-action-list__item">
                <button
                  class="pf-v6-c-button pf-m-circle pf-m-plain"
                  type="button"
                  aria-label="Help"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 32 32"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

```

### With drawer

This demo showcases how you can position a side-panel drawer on top of the other Compass elements.

```html isFullscreen isBeta
<div class="pf-v6-c-drawer pf-m-expanded pf-m-pill">
  <div class="pf-v6-c-drawer__main">
    <div class="pf-v6-c-drawer__content">
      <div class="pf-v6-c-drawer__body">
        <div class="pf-v6-c-compass pf-m-animate-smoothly">
          <div class="pf-v6-c-compass__container">
            <div class="pf-v6-c-compass__header pf-m-expanded">
              <div class="pf-v6-c-compass__logo">
                <svg
                  width="192"
                  height="39"
                  viewBox="0 0 192 39"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                  aria-hidden="true"
                >
                  <path
                    d="M33.3807 22.9001C36.6672 22.9001 41.4287 22.2167 41.4287 18.2926C41.4287 17.9865 41.4209 17.6883 41.3472 17.3901L39.3885 8.85069C38.9336 6.97444 38.5392 6.11944 35.2501 4.47014C32.7023 3.16125 27.1468 1 25.5035 1C23.9733 1 23.5211 2.98972 21.7069 2.98972C19.8927 2.98972 18.6465 1.51194 17.0032 1.51194C15.3599 1.51194 14.395 2.59389 13.6036 4.81056C13.6036 4.81056 11.3924 11.0674 11.1085 11.9778C11.0506 12.1493 11.0506 12.3393 11.0506 12.4897C11.0506 14.9228 20.5921 22.9001 33.3833 22.9001M41.9414 19.8839C42.3963 22.0451 42.3963 22.2721 42.3963 22.5571C42.3963 26.2542 38.2579 28.3019 32.818 28.3019C20.5185 28.3019 9.74918 21.0767 9.74918 16.3003C9.74918 15.5614 9.92008 14.8779 10.1462 14.366C5.72383 14.5929 0 15.3899 0 20.4539C0 28.7585 19.6114 39 35.1396 39C47.0421 39 50.0447 33.5956 50.0447 29.3285C50.0447 25.9718 47.1552 22.1612 41.9388 19.8839"
                    fill="#EE0000"
                  />
                  <path
                    d="M41.9386 19.8864C42.3935 22.0477 42.3935 22.2746 42.3935 22.5596C42.3935 26.2567 38.255 28.3045 32.8152 28.3045C20.5157 28.3045 9.74634 21.0792 9.74634 16.3028C9.74634 15.5639 9.91724 14.8804 10.1434 14.3685L11.1083 11.9777C11.0504 12.1492 11.0504 12.3392 11.0504 12.4896C11.0504 14.9227 20.5919 22.9 33.3831 22.9C36.6696 22.9 41.4312 22.2165 41.4312 18.2925C41.4312 17.9864 41.4233 17.6882 41.3496 17.39L41.9412 19.8864H41.9386Z"
                    fill="black"
                  />
                  <path
                    d="M75.764 16V1.29995H82.295C83.261 1.29995 84.115 1.48895 84.857 1.86695C85.599 2.24495 86.173 2.76995 86.579 3.44195C86.999 4.09995 87.209 4.86995 87.209 5.75195C87.209 6.70395 86.943 7.53695 86.411 8.25095C85.893 8.95095 85.186 9.46195 84.29 9.78395L87.398 16H84.605L81.77 10.12H78.284V16H75.764ZM78.284 8.10395H82.064C82.848 8.10395 83.478 7.89395 83.954 7.47395C84.43 7.03995 84.668 6.47295 84.668 5.77295C84.668 5.05895 84.43 4.49195 83.954 4.07195C83.478 3.63795 82.848 3.42095 82.064 3.42095H78.284V8.10395Z"
                    fill="var(--pf-t--global--text--color--regular)"
                  />
                  <path
                    d="M93.9392 16.21C92.9312 16.21 92.0212 15.972 91.2092 15.496C90.3972 15.006 89.7532 14.3549 89.2772 13.5429C88.8012 12.7169 88.5632 11.7859 88.5632 10.75C88.5632 9.71395 88.7872 8.78995 89.2352 7.97795C89.6832 7.16595 90.2922 6.52195 91.0622 6.04595C91.8462 5.55595 92.7142 5.31095 93.6662 5.31095C94.6462 5.31095 95.5072 5.54895 96.2492 6.02495C97.0052 6.50095 97.5932 7.14495 98.0132 7.95695C98.4472 8.76895 98.6642 9.69995 98.6642 10.75V11.3169H90.8942C90.9782 11.8909 91.1602 12.4019 91.4402 12.8499C91.7342 13.2839 92.1052 13.627 92.5532 13.879C93.0152 14.1309 93.5122 14.257 94.0442 14.257C94.5342 14.257 94.9962 14.173 95.4302 14.005C95.8782 13.823 96.2492 13.578 96.5432 13.2699L98.0972 14.677C97.4532 15.209 96.7952 15.601 96.1232 15.853C95.4652 16.091 94.7372 16.21 93.9392 16.21ZM90.9152 9.84695H96.4172C96.3332 9.34295 96.1582 8.89495 95.8922 8.50295C95.6402 8.11095 95.3182 7.80295 94.9262 7.57895C94.5482 7.35495 94.1282 7.24295 93.6662 7.24295C93.2042 7.24295 92.7772 7.35495 92.3852 7.57895C92.0072 7.78895 91.6922 8.08995 91.4402 8.48195C91.1882 8.87395 91.0132 9.32895 90.9152 9.84695Z"
                    fill="var(--pf-t--global--text--color--regular)"
                  />
                  <path
                    d="M105.388 16.1049C104.506 16.1049 103.708 15.867 102.994 15.391C102.28 14.901 101.706 14.257 101.272 13.459C100.852 12.6469 100.642 11.7439 100.642 10.75C100.642 9.74195 100.859 8.83895 101.293 8.04095C101.727 7.22895 102.315 6.58495 103.057 6.10895C103.813 5.63295 104.646 5.39495 105.556 5.39495C106.158 5.39495 106.718 5.51395 107.236 5.75195C107.768 5.97595 108.23 6.31195 108.622 6.75995V0.94295L110.995 0.522949V16H108.643V14.6139C108.265 15.0899 107.796 15.461 107.236 15.727C106.676 15.979 106.06 16.1049 105.388 16.1049ZM106.123 14.11C106.627 14.11 107.096 14.012 107.53 13.816C107.964 13.606 108.328 13.319 108.622 12.955V8.52395C108.314 8.15995 107.943 7.87995 107.509 7.68395C107.075 7.48795 106.613 7.38995 106.123 7.38995C105.521 7.38995 104.982 7.53695 104.506 7.83095C104.044 8.11095 103.673 8.50295 103.393 9.00695C103.113 9.51095 102.973 10.092 102.973 10.75C102.973 11.38 103.113 11.9539 103.393 12.4719C103.673 12.976 104.044 13.375 104.506 13.669C104.982 13.9629 105.521 14.11 106.123 14.11Z"
                    fill="var(--pf-t--global--text--color--regular)"
                  />
                  <path
                    d="M118.848 16V1.29995H121.368V7.47395H128.676V1.29995H131.196V16H128.676V9.72095H121.368V16H118.848Z"
                    fill="var(--pf-t--global--text--color--regular)"
                  />
                  <path
                    d="M137.314 16.189C136.586 16.189 135.935 16.056 135.361 15.79C134.801 15.51 134.36 15.132 134.038 14.656C133.73 14.166 133.576 13.606 133.576 12.976C133.576 12.346 133.737 11.7999 134.059 11.3379C134.395 10.8759 134.864 10.519 135.466 10.267C136.068 10.015 136.782 9.88895 137.608 9.88895C138.098 9.88895 138.581 9.94495 139.057 10.0569C139.533 10.1549 139.995 10.323 140.443 10.561V9.38495C140.443 8.68495 140.24 8.15995 139.834 7.80995C139.442 7.45995 138.84 7.28495 138.028 7.28495C137.594 7.28495 137.125 7.35495 136.621 7.49495C136.131 7.62095 135.578 7.82395 134.962 8.10395L134.122 6.38195C135.662 5.66795 137.118 5.31095 138.49 5.31095C139.862 5.31095 140.919 5.64695 141.661 6.31895C142.417 6.97695 142.795 7.91495 142.795 9.13295V16H140.443V14.908C139.995 15.342 139.512 15.6639 138.994 15.874C138.476 16.084 137.916 16.189 137.314 16.189ZM135.802 12.934C135.802 13.424 135.998 13.809 136.39 14.089C136.782 14.3689 137.307 14.509 137.965 14.509C138.441 14.509 138.882 14.439 139.288 14.299C139.708 14.1449 140.093 13.9209 140.443 13.627V11.926C140.079 11.7579 139.701 11.6319 139.309 11.5479C138.917 11.464 138.49 11.422 138.028 11.422C137.342 11.422 136.796 11.5549 136.39 11.8209C135.998 12.0869 135.802 12.458 135.802 12.934Z"
                    fill="var(--pf-t--global--text--color--regular)"
                  />
                  <path
                    d="M149.897 16.21C148.833 16.21 148.028 15.9649 147.482 15.4749C146.936 14.971 146.663 14.236 146.663 13.2699V7.36895H144.563V5.47895H146.663V2.58095L149.036 2.07695V5.47895H151.955V7.36895H149.036V12.745C149.036 13.2629 149.148 13.634 149.372 13.858C149.596 14.068 149.974 14.1729 150.506 14.1729C150.744 14.1729 150.961 14.1589 151.157 14.1309C151.367 14.089 151.626 14.0189 151.934 13.9209V15.9159C151.64 16.0139 151.304 16.084 150.926 16.1259C150.562 16.1819 150.219 16.21 149.897 16.21Z"
                    fill="var(--pf-t--global--text--color--regular)"
                  />
                  <path
                    d="M73.916 38L79.964 23.2999H83.471L89.456 38H86.159L84.668 34.1359H78.599L77.087 38H73.916ZM79.544 31.6999H83.744L81.644 26.2819L79.544 31.6999Z"
                    fill="var(--pf-t--global--text--color--regular)"
                  />
                  <path
                    d="M94.4493 38.2099C93.6093 38.2099 92.8603 38.028 92.2023 37.664C91.5583 37.286 91.0473 36.768 90.6693 36.11C90.3053 35.452 90.1233 34.6959 90.1233 33.8419V27.059H93.0003V33.422C93.0003 34.122 93.2033 34.682 93.6093 35.102C94.0293 35.522 94.5823 35.7319 95.2683 35.7319C96.2483 35.7319 97.0043 35.368 97.5363 34.6399V27.059H100.413V38H97.5363V37.118C96.6963 37.846 95.6673 38.2099 94.4493 38.2099Z"
                    fill="var(--pf-t--global--text--color--regular)"
                  />
                  <path
                    d="M107.842 38.1679C106.625 38.1679 105.7 37.895 105.07 37.3489C104.454 36.7889 104.146 35.9769 104.146 34.9129V29.4529H101.899V27.059H104.146V24.2659L107.024 23.6149V27.059H110.153V29.4529H107.024V34.325C107.024 34.829 107.136 35.193 107.36 35.417C107.583 35.6269 107.975 35.7319 108.535 35.7319C108.815 35.7319 109.068 35.7179 109.292 35.6899C109.529 35.6479 109.789 35.5779 110.069 35.4799V37.853C109.775 37.951 109.404 38.028 108.956 38.084C108.522 38.1399 108.15 38.1679 107.842 38.1679Z"
                    fill="var(--pf-t--global--text--color--regular)"
                  />
                  <path
                    d="M116.767 38.2099C115.675 38.2099 114.688 37.958 113.806 37.4539C112.924 36.9499 112.224 36.271 111.706 35.417C111.188 34.563 110.929 33.604 110.929 32.54C110.929 31.476 111.188 30.517 111.706 29.663C112.224 28.795 112.924 28.1089 113.806 27.6049C114.688 27.101 115.675 26.8489 116.767 26.8489C117.859 26.8489 118.846 27.101 119.728 27.6049C120.61 28.1089 121.31 28.795 121.828 29.663C122.346 30.517 122.605 31.476 122.605 32.54C122.605 33.604 122.346 34.563 121.828 35.417C121.31 36.271 120.61 36.9499 119.728 37.4539C118.846 37.958 117.859 38.2099 116.767 38.2099ZM116.767 35.7109C117.341 35.7109 117.852 35.5709 118.3 35.291C118.762 35.011 119.126 34.6329 119.392 34.1569C119.672 33.6669 119.812 33.128 119.812 32.54C119.812 31.938 119.672 31.399 119.392 30.923C119.126 30.447 118.762 30.069 118.3 29.7889C117.852 29.4949 117.341 29.3479 116.767 29.3479C116.207 29.3479 115.696 29.4949 115.234 29.7889C114.772 30.069 114.408 30.447 114.142 30.923C113.876 31.399 113.743 31.938 113.743 32.54C113.743 33.128 113.876 33.6669 114.142 34.1569C114.408 34.6329 114.772 35.011 115.234 35.291C115.696 35.5709 116.207 35.7109 116.767 35.7109Z"
                    fill="var(--pf-t--global--text--color--regular)"
                  />
                  <path
                    d="M124.373 38V27.059H127.25V27.8989C128.034 27.1989 128.986 26.8489 130.106 26.8489C130.82 26.8489 131.457 26.996 132.017 27.2899C132.577 27.57 133.039 27.969 133.403 28.4869C134.313 27.3949 135.517 26.8489 137.015 26.8489C137.841 26.8489 138.562 27.038 139.178 27.416C139.808 27.78 140.298 28.291 140.648 28.9489C141.012 29.5929 141.194 30.3489 141.194 31.2169V38H138.338V31.6369C138.338 30.9229 138.149 30.3629 137.771 29.9569C137.393 29.5369 136.889 29.327 136.259 29.327C135.377 29.327 134.677 29.6909 134.159 30.4189C134.173 30.5449 134.187 30.6709 134.201 30.7969C134.215 30.9229 134.222 31.063 134.222 31.2169V38H131.345V31.6369C131.345 30.9229 131.156 30.3629 130.778 29.9569C130.414 29.5369 129.917 29.327 129.287 29.327C128.405 29.327 127.726 29.6629 127.25 30.3349V38H124.373Z"
                    fill="var(--pf-t--global--text--color--regular)"
                  />
                  <path
                    d="M146.87 38.1889C146.086 38.1889 145.393 38.049 144.791 37.769C144.189 37.475 143.72 37.076 143.384 36.5719C143.048 36.0679 142.88 35.4869 142.88 34.8289C142.88 33.7789 143.272 32.9669 144.056 32.393C144.854 31.805 145.946 31.511 147.332 31.511C148.284 31.511 149.18 31.6579 150.02 31.952V31.1539C150.02 29.8799 149.25 29.243 147.71 29.243C147.248 29.243 146.751 29.32 146.219 29.4739C145.687 29.6139 145.071 29.8379 144.371 30.146L143.321 28.025C144.189 27.6329 145.015 27.3389 145.799 27.143C146.597 26.947 147.395 26.8489 148.193 26.8489C149.663 26.8489 150.804 27.2059 151.616 27.92C152.442 28.62 152.855 29.6139 152.855 30.9019V38H150.02V37.2229C149.572 37.5589 149.089 37.804 148.571 37.958C148.053 38.1119 147.486 38.1889 146.87 38.1889ZM145.61 34.7659C145.61 35.186 145.792 35.5219 146.156 35.7739C146.52 36.0119 147.003 36.131 147.605 36.131C148.571 36.131 149.376 35.893 150.02 35.417V33.8209C149.32 33.541 148.55 33.401 147.71 33.401C147.052 33.401 146.534 33.527 146.156 33.7789C145.792 34.0169 145.61 34.346 145.61 34.7659Z"
                    fill="var(--pf-t--global--text--color--regular)"
                  />
                  <path
                    d="M159.912 38.1679C158.694 38.1679 157.77 37.895 157.14 37.3489C156.524 36.7889 156.216 35.9769 156.216 34.9129V29.4529H153.969V27.059H156.216V24.2659L159.093 23.6149V27.059H162.222V29.4529H159.093V34.325C159.093 34.829 159.205 35.193 159.429 35.417C159.653 35.6269 160.045 35.7319 160.605 35.7319C160.885 35.7319 161.137 35.7179 161.361 35.6899C161.599 35.6479 161.858 35.5779 162.138 35.4799V37.853C161.844 37.951 161.473 38.028 161.025 38.084C160.591 38.1399 160.22 38.1679 159.912 38.1679Z"
                    fill="var(--pf-t--global--text--color--regular)"
                  />
                  <path
                    d="M163.625 38V27.059H166.502V38H163.625ZM165.053 25.757C164.605 25.757 164.22 25.596 163.898 25.274C163.576 24.952 163.415 24.5669 163.415 24.1189C163.415 23.6569 163.576 23.2719 163.898 22.9639C164.22 22.6419 164.605 22.4809 165.053 22.4809C165.515 22.4809 165.9 22.6419 166.208 22.9639C166.53 23.2719 166.691 23.6569 166.691 24.1189C166.691 24.5669 166.53 24.952 166.208 25.274C165.9 25.596 165.515 25.757 165.053 25.757Z"
                    fill="var(--pf-t--global--text--color--regular)"
                  />
                  <path
                    d="M174.086 38.2099C172.994 38.2099 172.007 37.958 171.125 37.4539C170.243 36.9499 169.543 36.271 169.025 35.417C168.507 34.563 168.248 33.604 168.248 32.54C168.248 31.476 168.507 30.517 169.025 29.663C169.543 28.795 170.243 28.1089 171.125 27.6049C172.007 27.101 172.994 26.8489 174.086 26.8489C175.178 26.8489 176.165 27.101 177.047 27.6049C177.929 28.1089 178.629 28.795 179.147 29.663C179.665 30.517 179.924 31.476 179.924 32.54C179.924 33.604 179.665 34.563 179.147 35.417C178.629 36.271 177.929 36.9499 177.047 37.4539C176.165 37.958 175.178 38.2099 174.086 38.2099ZM174.086 35.7109C174.66 35.7109 175.171 35.5709 175.619 35.291C176.081 35.011 176.445 34.6329 176.711 34.1569C176.991 33.6669 177.131 33.128 177.131 32.54C177.131 31.938 176.991 31.399 176.711 30.923C176.445 30.447 176.081 30.069 175.619 29.7889C175.171 29.4949 174.66 29.3479 174.086 29.3479C173.526 29.3479 173.015 29.4949 172.553 29.7889C172.091 30.069 171.727 30.447 171.461 30.923C171.195 31.399 171.062 31.938 171.062 32.54C171.062 33.128 171.195 33.6669 171.461 34.1569C171.727 34.6329 172.091 35.011 172.553 35.291C173.015 35.5709 173.526 35.7109 174.086 35.7109Z"
                    fill="var(--pf-t--global--text--color--regular)"
                  />
                  <path
                    d="M181.693 38V27.059H184.57V27.962C185.396 27.2199 186.418 26.8489 187.636 26.8489C188.49 26.8489 189.239 27.038 189.883 27.416C190.541 27.78 191.052 28.291 191.416 28.9489C191.78 29.5929 191.962 30.3489 191.962 31.2169V38H189.085V31.6369C189.085 30.9229 188.882 30.3629 188.476 29.9569C188.07 29.5369 187.517 29.327 186.817 29.327C186.327 29.327 185.893 29.425 185.515 29.621C185.137 29.803 184.822 30.0689 184.57 30.4189V38H181.693Z"
                    fill="var(--pf-t--global--text--color--regular)"
                  />
                  <line
                    x1="66.5"
                    y1="1.5"
                    x2="66.5"
                    y2="38.5"
                    stroke="var(--pf-t--global--text--color--regular)"
                    stroke-linecap="round"
                  />
                </svg>
              </div>
              <div class="pf-v6-c-compass__nav">
                <div class="pf-v6-c-panel pf-m-pill pf-m-glass">
                  <div class="pf-v6-c-panel__main">
                    <div class="pf-v6-c-panel__main-body">
                      <div class="pf-v6-c-compass__nav-content">
                        <div class="pf-v6-c-compass__nav-home">
                          <button
                            class="pf-v6-c-button pf-m-circle pf-m-plain"
                            type="button"
                            aria-label="Home"
                          >
                            <span class="pf-v6-c-button__icon">
                              <svg
                                class="pf-v6-svg"
                                viewBox="0 0 32 32"
                                fill="currentColor"
                                aria-hidden="true"
                                role="img"
                                width="1em"
                                height="1em"
                              >
                                <path
                                  d="M30.707 15.435 17.061 1.789a1.501 1.501 0 0 0-2.121 0L1.293 15.435a.999.999 0 1 0 1.414 1.414L3 16.556V29.5c0 .827.673 1.5 1.5 1.5h23c.827 0 1.5-.673 1.5-1.5V16.556l.293.293a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414ZM19 29h-6V19h6v10Zm8-10v10h-6V18.5c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5V29H5V14.556l11-11 11 11V19Z"
                                />
                              </svg>
                            </span>
                          </button>
                        </div>
                        <div class="pf-v6-c-compass__nav-main">
                          <nav
                            class="pf-v6-c-tabs pf-m-nav"
                            aria-label="Compass primary"
                          >
                            <div
                              class="pf-v6-c-tabs__scroll-button"
                              aria-hidden="true"
                            >
                              <button
                                class="pf-v6-c-button pf-m-small pf-m-plain"
                                type="button"
                                aria-label="Scroll left"
                                disabled
                              >
                                <span class="pf-v6-c-button__icon">
                                  <svg
                                    class="pf-v6-svg"
                                    viewBox="0 0 20 20"
                                    fill="currentColor"
                                    aria-hidden="true"
                                    role="img"
                                    width="1em"
                                    height="1em"
                                  >
                                    <path
                                      d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                                    />
                                  </svg>
                                </span>
                              </button>
                            </div>
                            <ul
                              class="pf-v6-c-tabs__list"
                              role="tablist"
                              aria-label="Compass primary"
                            >
                              <li
                                class="pf-v6-c-tabs__item"
                                role="presentation"
                              >
                                <a
                                  class="pf-v6-c-tabs__link"
                                  href="#"
                                  role="tab"
                                  aria-selected="false"
                                  id="primary-nav-users-link"
                                >
                                  <span class="pf-v6-c-tabs__item-text">Users</span>
                                </a>
                              </li>
                              <li
                                class="pf-v6-c-tabs__item pf-m-current"
                                role="presentation"
                              >
                                <a
                                  class="pf-v6-c-tabs__link"
                                  href="#"
                                  role="tab"
                                  aria-selected="true"
                                  id="primary-nav-containers-link"
                                >
                                  <span
                                    class="pf-v6-c-tabs__item-text"
                                  >Containers</span>
                                </a>
                              </li>
                              <li
                                class="pf-v6-c-tabs__item"
                                role="presentation"
                              >
                                <a
                                  class="pf-v6-c-tabs__link"
                                  href="#"
                                  role="tab"
                                  aria-selected="false"
                                  id="primary-nav-database-link"
                                >
                                  <span class="pf-v6-c-tabs__item-text">Database</span>
                                </a>
                              </li>

                              <li
                                class="pf-v6-c-tabs__item"
                                role="presentation"
                              >
                                <a
                                  class="pf-v6-c-tabs__link"
                                  href="#"
                                  role="tab"
                                  aria-selected="false"
                                  id="primary-nav-server-link"
                                >
                                  <span class="pf-v6-c-tabs__item-text">Server</span>
                                </a>
                              </li>
                              <li
                                class="pf-v6-c-tabs__item"
                                role="presentation"
                              >
                                <a
                                  class="pf-v6-c-tabs__link"
                                  href="#"
                                  role="tab"
                                  aria-selected="false"
                                  id="primary-nav-system-link"
                                >
                                  <span class="pf-v6-c-tabs__item-text">System</span>
                                </a>
                              </li>
                              <li
                                class="pf-v6-c-tabs__item"
                                role="presentation"
                              >
                                <a
                                  class="pf-v6-c-tabs__link"
                                  href="#"
                                  role="tab"
                                  aria-selected="false"
                                  id="primary-nav-network-wired-link"
                                >
                                  <span class="pf-v6-c-tabs__item-text">Network</span>
                                </a>
                              </li>
                            </ul>

                            <div
                              class="pf-v6-c-tabs__scroll-button"
                              aria-hidden="true"
                            >
                              <button
                                class="pf-v6-c-button pf-m-small pf-m-plain"
                                type="button"
                                aria-label="Scroll right"
                                disabled
                              >
                                <span class="pf-v6-c-button__icon">
                                  <svg
                                    class="pf-v6-svg"
                                    viewBox="0 0 20 20"
                                    fill="currentColor"
                                    aria-hidden="true"
                                    role="img"
                                    width="1em"
                                    height="1em"
                                  >
                                    <path
                                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                                    />
                                  </svg>
                                </span>
                              </button>
                            </div>
                          </nav>
                        </div>
                        <div class="pf-v6-c-compass__nav-search">
                          <button
                            class="pf-v6-c-button pf-m-circle pf-m-plain"
                            type="button"
                            aria-label="Search"
                          >
                            <span class="pf-v6-c-button__icon">
                              <svg
                                class="pf-v6-svg"
                                viewBox="0 0 32 32"
                                fill="currentColor"
                                aria-hidden="true"
                                role="img"
                                width="1em"
                                height="1em"
                              >
                                <path
                                  d="m30.796 29.205-8.557-8.557A11.945 11.945 0 0 0 25 13c0-6.617-5.383-12-12-12S1 6.383 1 13s5.383 12 12 12c2.904 0 5.57-1.038 7.648-2.761l8.556 8.556a1.122 1.122 0 0 0 1.592 0 1.127 1.127 0 0 0 0-1.591ZM3 13C3 7.486 7.486 3 13 3s10 4.486 10 10-4.486 10-10 10S3 18.514 3 13Z"
                                />
                              </svg>
                            </span>
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="pf-v6-c-panel pf-m-pill pf-m-glass">
                  <div class="pf-v6-c-panel__main">
                    <div class="pf-v6-c-panel__main-body">
                      <div class="pf-v6-c-compass__nav-content">
                        <div class="pf-v6-c-compass__nav-main">
                          <nav
                            class="pf-v6-c-tabs pf-m-nav pf-m-subtab"
                            aria-label="Compass secondary"
                          >
                            <div
                              class="pf-v6-c-tabs__scroll-button"
                              aria-hidden="true"
                            >
                              <button
                                class="pf-v6-c-button pf-m-small pf-m-plain"
                                type="button"
                                aria-label="Scroll left"
                                disabled
                              >
                                <span class="pf-v6-c-button__icon">
                                  <svg
                                    class="pf-v6-svg"
                                    viewBox="0 0 20 20"
                                    fill="currentColor"
                                    aria-hidden="true"
                                    role="img"
                                    width="1em"
                                    height="1em"
                                  >
                                    <path
                                      d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                                    />
                                  </svg>
                                </span>
                              </button>
                            </div>
                            <ul
                              class="pf-v6-c-tabs__list"
                              role="tablist"
                              aria-label="Compass secondary"
                            >
                              <li
                                class="pf-v6-c-tabs__item"
                                role="presentation"
                              >
                                <a
                                  class="pf-v6-c-tabs__link"
                                  href="#"
                                  role="tab"
                                  aria-selected="false"
                                  id="secondary-nav-sub-1-link"
                                >
                                  <span class="pf-v6-c-tabs__item-text">Item 1</span>
                                </a>
                              </li>
                              <li
                                class="pf-v6-c-tabs__item"
                                role="presentation"
                              >
                                <a
                                  class="pf-v6-c-tabs__link"
                                  href="#"
                                  role="tab"
                                  aria-selected="false"
                                  id="secondary-nav-sub-2-link"
                                >
                                  <span class="pf-v6-c-tabs__item-text">Item 2</span>
                                </a>
                              </li>
                              <li
                                class="pf-v6-c-tabs__item pf-m-current"
                                role="presentation"
                              >
                                <a
                                  class="pf-v6-c-tabs__link"
                                  href="#"
                                  role="tab"
                                  aria-selected="true"
                                  id="secondary-nav-sub-3-link"
                                >
                                  <span class="pf-v6-c-tabs__item-text">Item 3</span>
                                </a>
                              </li>

                              <li
                                class="pf-v6-c-tabs__item"
                                role="presentation"
                              >
                                <a
                                  class="pf-v6-c-tabs__link pf-m-disabled"
                                  aria-disabled="true"
                                  tabindex="-1"
                                  href="#"
                                  role="tab"
                                  aria-selected="false"
                                  id="secondary-nav-sub-disabled-link"
                                >
                                  <span class="pf-v6-c-tabs__item-text">Disabled</span>
                                </a>
                              </li>
                              <li
                                class="pf-v6-c-tabs__item"
                                role="presentation"
                              >
                                <a
                                  class="pf-v6-c-tabs__link pf-m-aria-disabled"
                                  aria-disabled="true"
                                  href="#"
                                  role="tab"
                                  aria-selected="false"
                                  id="secondary-nav-sub-aria-disabled-link"
                                >
                                  <span
                                    class="pf-v6-c-tabs__item-text"
                                  >ARIA disabled</span>
                                </a>
                              </li>
                              <li
                                class="pf-v6-c-tabs__item"
                                role="presentation"
                              >
                                <a
                                  class="pf-v6-c-tabs__link"
                                  href="#"
                                  role="tab"
                                  aria-selected="false"
                                  id="secondary-nav-sub-6-link"
                                >
                                  <span class="pf-v6-c-tabs__item-text">Item 6</span>
                                </a>
                              </li>
                            </ul>

                            <div
                              class="pf-v6-c-tabs__scroll-button"
                              aria-hidden="true"
                            >
                              <button
                                class="pf-v6-c-button pf-m-small pf-m-plain"
                                type="button"
                                aria-label="Scroll right"
                                disabled
                              >
                                <span class="pf-v6-c-button__icon">
                                  <svg
                                    class="pf-v6-svg"
                                    viewBox="0 0 20 20"
                                    fill="currentColor"
                                    aria-hidden="true"
                                    role="img"
                                    width="1em"
                                    height="1em"
                                  >
                                    <path
                                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                                    />
                                  </svg>
                                </span>
                              </button>
                            </div>
                          </nav>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="pf-v6-c-compass__profile">
                <button
                  class="pf-v6-c-menu-toggle pf-m-circle pf-m-text pf-m-plain"
                  type="button"
                  aria-expanded="false"
                >
                  <span class="pf-v6-c-menu-toggle__icon">
                    <img
                      class="pf-v6-c-avatar pf-m-md"
                      alt="Avatar image"
                      src="/assets/images/img_avatar-light.svg"
                    />
                  </span>
                  <span class="pf-v6-c-menu-toggle__text">Ned Username</span>
                  <span class="pf-v6-c-menu-toggle__controls">
                    <span class="pf-v6-c-menu-toggle__toggle-icon">
                      <svg
                        class="pf-v6-svg"
                        viewBox="0 0 20 20"
                        fill="currentColor"
                        aria-hidden="true"
                        role="img"
                        width="1em"
                        height="1em"
                      >
                        <path
                          d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
                        />
                      </svg>
                    </span>
                  </span>
                </button>
              </div>
            </div>
            <div class="pf-v6-c-compass__sidebar pf-m-expanded pf-m-start">
              <div class="pf-v6-c-panel pf-m-pill pf-m-glass">
                <div class="pf-v6-c-panel__main">
                  <div class="pf-v6-c-panel__main-body">
                    <div class="pf-v6-c-action-list pf-m-icons pf-m-vertical">
                      <div class="pf-v6-c-action-list__item">
                        <button
                          class="pf-v6-c-button pf-m-circle pf-m-plain"
                          type="button"
                          aria-label="Add"
                        >
                          <span class="pf-v6-c-button__icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M28.5 2h-25C2.673 2 2 2.673 2 3.5v25c0 .827.673 1.5 1.5 1.5h25c.827 0 1.5-.673 1.5-1.5v-25c0-.827-.673-1.5-1.5-1.5ZM28 28H4V4h24v24ZM8 16a1 1 0 0 1 1-1h6V9a1 1 0 1 1 2 0v6h6a1 1 0 1 1 0 2h-6v6a1 1 0 1 1-2 0v-6H9a1 1 0 0 1-1-1Z"
                              />
                            </svg>
                          </span>
                        </button>
                      </div>
                      <div class="pf-v6-c-action-list__item">
                        <button
                          class="pf-v6-c-button pf-m-circle pf-m-plain"
                          type="button"
                          aria-label="Collections"
                        >
                          <span class="pf-v6-c-button__icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M28.5 11h-25c-.827 0-1.5.673-1.5 1.5v17c0 .827.673 1.5 1.5 1.5h25c.827 0 1.5-.673 1.5-1.5v-17c0-.827-.673-1.5-1.5-1.5ZM28 29H4V13h24v16ZM6 2a1 1 0 0 1 1-1h18a1 1 0 0 1 0 2H7a1 1 0 0 1-1-1ZM4 7a1 1 0 0 1 1-1h22a1 1 0 0 1 0 2H5a1 1 0 0 1-1-1Z"
                              />
                            </svg>
                          </span>
                        </button>
                      </div>
                      <div class="pf-v6-c-action-list__item">
                        <button
                          class="pf-v6-c-button pf-v6-m-ai-indicator pf-m-circle pf-m-plain"
                          type="button"
                          aria-label="AI assistant"
                        >
                          <span class="pf-v6-c-button__icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M30.502 7c0 .29-.209.536-.498.59a5.523 5.523 0 0 0-4.417 4.417c-.054.289-.3.498-.59.498s-.536-.21-.59-.498A5.52 5.52 0 0 0 19.99 7.59c-.289-.054-.498-.3-.498-.59s.21-.536.498-.59a5.52 5.52 0 0 0 4.417-4.417c.054-.289.301-.498.59-.498s.536.21.59.498a5.523 5.523 0 0 0 4.417 4.417c.289.054.498.3.498.59Zm-4.465 9.962A11.932 11.932 0 0 1 15.038 5.97C15.001 5.447 14.524 5 14 5c-.521 0-.997.442-1.038.962a11.932 11.932 0 0 1-10.992 11C1.447 16.999 1 17.476 1 18c0 .521.442.997.962 1.038a11.932 11.932 0 0 1 11 10.992c.037.524.514.97 1.038.97.521 0 .997-.442 1.038-.962a11.933 11.933 0 0 1 11-10.999c.519-.042.961-.516.961-1.038 0-.521-.442-.997-.962-1.038Z"
                              />
                            </svg>
                          </span>
                        </button>
                      </div>
                      <div class="pf-v6-c-action-list__item">
                        <button
                          class="pf-v6-c-button pf-m-circle pf-m-plain"
                          type="button"
                          aria-label="Volume"
                        >
                          <span class="pf-v6-c-button__icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M17.439 2.102a1 1 0 0 0-1.054.109L7.656 9H2.5C1.673 9 1 9.673 1 10.5v11c0 .827.673 1.5 1.5 1.5h5.157l8.729 6.789a.998.998 0 0 0 1.053.109c.343-.168.561-.517.561-.898V3a1 1 0 0 0-.561-.898ZM16 26.955l-7.386-5.744A1 1 0 0 0 8 21H3V11h5a.997.997 0 0 0 .614-.211L16 5.045v21.91ZM31 16a14.94 14.94 0 0 1-4.284 10.488.997.997 0 0 1-1.414.018 1 1 0 0 1-.018-1.414C27.68 22.637 29 19.408 29 16s-1.319-6.637-3.716-9.092a.999.999 0 1 1 1.432-1.396A14.94 14.94 0 0 1 31 16Zm-6 0a9.007 9.007 0 0 1-2.249 5.95.996.996 0 0 1-1.411.091 1 1 0 0 1-.091-1.411C22.378 19.346 23 17.702 23 16s-.622-3.346-1.751-4.63a1 1 0 0 1 1.502-1.32A9.007 9.007 0 0 1 25 16Z"
                              />
                            </svg>
                          </span>
                        </button>
                      </div>
                      <div class="pf-v6-c-action-list__item">
                        <button
                          class="pf-v6-c-button pf-m-circle pf-m-plain"
                          type="button"
                          aria-label="Use microphone"
                        >
                          <span class="pf-v6-c-button__icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M16 22c3.86 0 7-3.141 7-7V8c0-3.859-3.14-7-7-7S9 4.141 9 8v7c0 3.859 3.14 7 7 7ZM11 8c0-2.757 2.243-5 5-5s5 2.243 5 5v7c0 2.757-2.243 5-5 5s-5-2.243-5-5V8Zm5.99 17.95c0 .018.01.032.01.05v2.021h5a1 1 0 1 1 0 2H10.02a1 1 0 1 1 0-2H15V26c0-.018.009-.033.01-.05C9.407 25.447 5 20.731 5 15a1 1 0 1 1 2 0c0 4.963 4.038 9 9 9s9-4.037 9-9a1 1 0 1 1 2 0c0 5.731-4.407 10.447-10.01 10.95Z"
                              />
                            </svg>
                          </span>
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="pf-v6-c-compass__main">
              <div class="pf-v6-c-compass__main-header">
                <div class="pf-v6-c-panel pf-m-glass">
                  <div class="pf-v6-c-panel__main">
                    <div class="pf-v6-c-panel__main-body">
                      <div class="pf-v6-c-compass__main-header-content">
                        <div class="pf-v6-c-compass__main-header-title">
                          <h2 class="pf-v6-c-title pf-m-h1">Page title</h2>
                        </div>
                        <div class="pf-v6-c-compass__main-header-toolbar">
                          <div class="pf-v6-c-action-list">
                            <div class="pf-v6-c-action-list__group">
                              <div class="pf-v6-c-action-list__item">
                                <button
                                  class="pf-v6-c-button pf-m-primary"
                                  type="button"
                                >
                                  <span
                                    class="pf-v6-c-button__text"
                                  >Add integration</span>
                                </button>
                              </div>
                              <div class="pf-v6-c-action-list__item">
                                <button
                                  class="pf-v6-c-button pf-m-secondary"
                                  type="button"
                                >
                                  <span
                                    class="pf-v6-c-button__text"
                                  >Test integration</span>
                                </button>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="pf-v6-c-compass__content">
                <div
                  class="pf-v6-c-panel pf-m-glass pf-m-scrollable-auto-height pf-m-scrollable"
                >
                  <div class="pf-v6-c-panel__main">
                    <div class="pf-v6-c-panel__main-body">
                      <div class="pf-v6-l-flex pf-m-column pf-m-gap-md">
                        <div class="pf-v6-c-toolbar" id="-toolbar">
                          <div class="pf-v6-c-toolbar__content">
                            <div
                              class="pf-v6-c-toolbar__content-section pf-m-nowrap"
                            >
                              <div
                                class="pf-v6-c-toolbar__group pf-m-show-on-xl pf-m-toggle-group"
                              >
                                <div class="pf-v6-c-toolbar__toggle">
                                  <button
                                    class="pf-v6-c-menu-toggle pf-m-plain"
                                    type="button"
                                    aria-expanded="false"
                                    aria-label="Show filters"
                                    aria-controls="-toolbar-expandable-content"
                                  >
                                    <span class="pf-v6-c-menu-toggle__icon">
                                      <svg
                                        class="pf-v6-svg"
                                        viewBox="0 0 32 32"
                                        fill="currentColor"
                                        aria-hidden="true"
                                        role="img"
                                        width="1em"
                                        height="1em"
                                      >
                                        <path
                                          d="M29.875 3.5V7a.876.876 0 0 1-.256.619l-9.744 9.744v10.638a.875.875 0 0 1-.599.83l-6 2a.876.876 0 0 1-.788-.12.874.874 0 0 1-.363-.71V17.363L2.381 7.619A.876.876 0 0 1 2.125 7V3.5c0-.758.617-1.375 1.375-1.375h25c.758 0 1.375.617 1.375 1.375Z"
                                        />
                                      </svg>
                                    </span>
                                  </button>
                                </div>
                                <div
                                  class="pf-v6-c-toolbar__item pf-m-bulk-select"
                                >
                                  <div
                                    class="pf-v6-c-menu-toggle pf-m-split-button"
                                    id="-toolbar-check"
                                  >
                                    <label
                                      class="pf-v6-c-check pf-m-standalone"
                                      for="-toolbar-check-check-input"
                                    >
                                      <input
                                        class="pf-v6-c-check__input"
                                        type="checkbox"
                                        id="-toolbar-check-check-input"
                                        name="-toolbar-check-check-input"
                                        aria-label="Standalone check"
                                      />
                                    </label>
                                    <button
                                      class="pf-v6-c-menu-toggle__button"
                                      type="button"
                                      aria-expanded="false"
                                      id="-toolbar-menu-toggle-toggle-button"
                                      aria-label="Menu toggle"
                                    >
                                      <span
                                        class="pf-v6-c-menu-toggle__controls"
                                      >
                                        <span
                                          class="pf-v6-c-menu-toggle__toggle-icon"
                                        >
                                          <svg
                                            class="pf-v6-svg"
                                            viewBox="0 0 20 20"
                                            fill="currentColor"
                                            aria-hidden="true"
                                            role="img"
                                            width="1em"
                                            height="1em"
                                          >
                                            <path
                                              d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
                                            />
                                          </svg>
                                        </span>
                                      </span>
                                    </button>
                                  </div>
                                </div>

                                <div class="pf-v6-c-toolbar__item">
                                  <button
                                    class="pf-v6-c-menu-toggle"
                                    type="button"
                                    aria-expanded="false"
                                    id="-toolbar-select-checkbox-status"
                                  >
                                    <span
                                      class="pf-v6-c-menu-toggle__text"
                                    >Status</span>
                                    <span class="pf-v6-c-menu-toggle__controls">
                                      <span
                                        class="pf-v6-c-menu-toggle__toggle-icon"
                                      >
                                        <svg
                                          class="pf-v6-svg"
                                          viewBox="0 0 20 20"
                                          fill="currentColor"
                                          aria-hidden="true"
                                          role="img"
                                          width="1em"
                                          height="1em"
                                        >
                                          <path
                                            d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
                                          />
                                        </svg>
                                      </span>
                                    </span>
                                  </button>
                                </div>
                              </div>

                              <div
                                class="pf-v6-c-overflow-menu"
                                id="-toolbar-overflow-menu"
                              >
                                <div
                                  class="pf-v6-c-overflow-menu__content pf-v6-u-display-none pf-v6-u-display-flex-on-lg"
                                >
                                  <div
                                    class="pf-v6-c-overflow-menu__group pf-m-button-group"
                                  >
                                    <div class="pf-v6-c-overflow-menu__item">
                                      <button
                                        class="pf-v6-c-button pf-m-primary"
                                        type="button"
                                      >
                                        <span
                                          class="pf-v6-c-button__text"
                                        >Create instance</span>
                                      </button>
                                    </div>
                                  </div>
                                </div>
                                <div class="pf-v6-c-overflow-menu__control">
                                  <button
                                    class="pf-v6-c-menu-toggle pf-m-plain"
                                    type="button"
                                    aria-expanded="false"
                                    aria-label="Menu toggle"
                                    id="-toolbar-overflow-menu-toggle"
                                  >
                                    <span class="pf-v6-c-menu-toggle__icon">
                                      <svg
                                        class="pf-v6-svg"
                                        viewBox="0 0 32 32"
                                        fill="currentColor"
                                        aria-hidden="true"
                                        role="img"
                                        width="1em"
                                        height="1em"
                                      >
                                        <path
                                          d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                        />
                                      </svg>
                                    </span>
                                  </button>
                                </div>
                              </div>

                              <div
                                class="pf-v6-c-toolbar__item pf-m-pagination"
                              >
                                <div class="pf-v6-c-pagination pf-m-compact">
                                  <div class="pf-v6-c-pagination__page-menu">
                                    <button
                                      class="pf-v6-c-menu-toggle pf-m-text pf-m-plain"
                                      type="button"
                                      aria-expanded="false"
                                      id="-toolbar-top-pagination"
                                    >
                                      <span class="pf-v6-c-menu-toggle__text">
                                        <b>1 - 10</b>&nbsp;of&nbsp;
                                        <b>36</b>
                                      </span>
                                      <span
                                        class="pf-v6-c-menu-toggle__controls"
                                      >
                                        <span
                                          class="pf-v6-c-menu-toggle__toggle-icon"
                                        >
                                          <svg
                                            class="pf-v6-svg"
                                            viewBox="0 0 20 20"
                                            fill="currentColor"
                                            aria-hidden="true"
                                            role="img"
                                            width="1em"
                                            height="1em"
                                          >
                                            <path
                                              d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
                                            />
                                          </svg>
                                        </span>
                                      </span>
                                    </button>
                                  </div>
                                  <nav
                                    class="pf-v6-c-pagination__nav"
                                    aria-label="Toolbar top pagination"
                                  >
                                    <div
                                      class="pf-v6-c-pagination__nav-control pf-m-prev"
                                    >
                                      <button
                                        class="pf-v6-c-button pf-m-plain"
                                        type="button"
                                        disabled
                                        aria-label="Go to previous page"
                                      >
                                        <span class="pf-v6-c-button__icon">
                                          <svg
                                            class="pf-v6-svg"
                                            viewBox="0 0 256 512"
                                            fill="currentColor"
                                            aria-hidden="true"
                                            role="img"
                                            width="1em"
                                            height="1em"
                                          >
                                            <path
                                              d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
                                            />
                                          </svg>
                                        </span>
                                      </button>
                                    </div>
                                    <div
                                      class="pf-v6-c-pagination__nav-control pf-m-next"
                                    >
                                      <button
                                        class="pf-v6-c-button pf-m-plain"
                                        type="button"
                                        aria-label="Go to next page"
                                      >
                                        <span class="pf-v6-c-button__icon">
                                          <svg
                                            class="pf-v6-svg"
                                            viewBox="0 0 256 512"
                                            fill="currentColor"
                                            aria-hidden="true"
                                            role="img"
                                            width="1em"
                                            height="1em"
                                          >
                                            <path
                                              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
                                            />
                                          </svg>
                                        </span>
                                      </button>
                                    </div>
                                  </nav>
                                </div>
                              </div>
                            </div>

                            <div
                              class="pf-v6-c-toolbar__expandable-content pf-m-hidden"
                              id="-toolbar-expandable-content"
                              hidden
                            ></div>
                          </div>
                        </div>
                        <div class="pf-v6-l-gallery pf-m-gutter">
                          <div
                            class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                            id="card-view-basic-example-gallery-card-empty-state"
                          >
                            <div class="pf-v6-l-bullseye">
                              <div class="pf-v6-c-empty-state pf-m-xs">
                                <div class="pf-v6-c-empty-state__content">
                                  <div class="pf-v6-c-empty-state__icon">
                                    <svg
                                      class="pf-v6-svg"
                                      viewBox="0 0 32 32"
                                      fill="currentColor"
                                      aria-hidden="true"
                                      role="img"
                                      width="1em"
                                      height="1em"
                                    >
                                      <path
                                        d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7 16.125h-5.875V23a1.125 1.125 0 0 1-2.25 0v-5.875H9a1.125 1.125 0 0 1 0-2.25h5.875V9a1.125 1.125 0 0 1 2.25 0v5.875H23a1.125 1.125 0 0 1 0 2.25Z"
                                      />
                                    </svg>
                                  </div>
                                  <div class="pf-v6-c-card__title">
                                    <h2
                                      class="pf-v6-c-card__title-text pf-m-md"
                                    >Add a new card to your page</h2>
                                  </div>
                                  <button
                                    class="pf-v6-c-button pf-m-link"
                                    type="button"
                                  >
                                    <span class="pf-v6-c-button__text">Add card</span>
                                  </button>
                                </div>
                              </div>
                            </div>
                          </div>
                          <div
                            class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                            id="card-view-basic-example-gallery-card-1"
                          >
                            <div class="pf-v6-c-card__header">
                              <img
                                src="/assets/images/PF-IconLogo.svg"
                                alt="PatternFly logo"
                              />
                              <div class="pf-v6-c-card__actions">
                                <button
                                  class="pf-v6-c-menu-toggle pf-m-plain"
                                  type="button"
                                  aria-expanded="false"
                                  aria-label="Menu toggle"
                                  id="card-view-basic-example-gallery-card-1-toggle"
                                >
                                  <span class="pf-v6-c-menu-toggle__icon">
                                    <svg
                                      class="pf-v6-svg"
                                      viewBox="0 0 32 32"
                                      fill="currentColor"
                                      aria-hidden="true"
                                      role="img"
                                      width="1em"
                                      height="1em"
                                    >
                                      <path
                                        d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                      />
                                    </svg>
                                  </span>
                                </button>
                                <div class="pf-v6-c-check pf-m-standalone">
                                  <input
                                    class="pf-v6-c-check__input"
                                    type="checkbox"
                                    id="card-view-basic-example-gallery-card-1-check"
                                    name="card-view-basic-example-gallery-card-1-check"
                                    aria-labelledby="card-view-basic-example-gallery-card-1-check-label"
                                  />
                                </div>
                              </div>
                            </div>
                            <div class="pf-v6-c-card__title">
                              <h2
                                class="pf-v6-c-card__title-text"
                                id="card-view-basic-example-gallery-card-1-check-label"
                              >Patternfly</h2>
                              <div class="pf-v6-c-content">
                                <small>Provided by Red Hat</small>
                              </div>
                            </div>
                            <div
                              class="pf-v6-c-card__body"
                            >PatternFly is a community project that promotes design commonality and improves user experience.</div>
                          </div>
                          <div
                            class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                            id="card-view-basic-example-gallery-card-2"
                          >
                            <div class="pf-v6-c-card__header">
                              <img
                                src="/assets/images/activemq-core_200x150.png"
                                width="60px"
                                alt="Logo"
                              />
                              <div class="pf-v6-c-card__actions">
                                <button
                                  class="pf-v6-c-menu-toggle pf-m-plain"
                                  type="button"
                                  aria-expanded="false"
                                  aria-label="Menu toggle"
                                  id="card-view-basic-example-gallery-card-2-toggle"
                                >
                                  <span class="pf-v6-c-menu-toggle__icon">
                                    <svg
                                      class="pf-v6-svg"
                                      viewBox="0 0 32 32"
                                      fill="currentColor"
                                      aria-hidden="true"
                                      role="img"
                                      width="1em"
                                      height="1em"
                                    >
                                      <path
                                        d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                      />
                                    </svg>
                                  </span>
                                </button>
                                <div class="pf-v6-c-check pf-m-standalone">
                                  <input
                                    class="pf-v6-c-check__input"
                                    type="checkbox"
                                    id="card-view-basic-example-gallery-card-2-check"
                                    name="card-view-basic-example-gallery-card-2-check"
                                    aria-labelledby="card-view-basic-example-gallery-card-2-check-label"
                                  />
                                </div>
                              </div>
                            </div>
                            <div class="pf-v6-c-card__title">
                              <h2
                                class="pf-v6-c-card__title-text"
                                id="card-view-basic-example-gallery-card-2-check-label"
                              >ActiveMq</h2>
                              <div class="pf-v6-c-content">
                                <small>Provided by Red Hat</small>
                              </div>
                            </div>
                            <div
                              class="pf-v6-c-card__body"
                            >The ActiveMQ component allows messages to be sent to a JMS Queue or Topic; or messages to be consumed from a JMS Queue or Topic using Apache ActiveMQ.</div>
                          </div>
                          <div
                            class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                            id="card-view-basic-example-gallery-card-3"
                          >
                            <div class="pf-v6-c-card__header">
                              <img
                                src="/assets/images/camel-spark_200x150.png"
                                width="60px"
                                alt="Logo"
                              />
                              <div class="pf-v6-c-card__actions">
                                <button
                                  class="pf-v6-c-menu-toggle pf-m-plain"
                                  type="button"
                                  aria-expanded="false"
                                  aria-label="Menu toggle"
                                  id="card-view-basic-example-gallery-card-3-toggle"
                                >
                                  <span class="pf-v6-c-menu-toggle__icon">
                                    <svg
                                      class="pf-v6-svg"
                                      viewBox="0 0 32 32"
                                      fill="currentColor"
                                      aria-hidden="true"
                                      role="img"
                                      width="1em"
                                      height="1em"
                                    >
                                      <path
                                        d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                      />
                                    </svg>
                                  </span>
                                </button>
                                <div class="pf-v6-c-check pf-m-standalone">
                                  <input
                                    class="pf-v6-c-check__input"
                                    type="checkbox"
                                    id="card-view-basic-example-gallery-card-3-check"
                                    name="card-view-basic-example-gallery-card-3-check"
                                    aria-labelledby="card-view-basic-example-gallery-card-3-check-label"
                                  />
                                </div>
                              </div>
                            </div>
                            <div class="pf-v6-c-card__title">
                              <h2
                                class="pf-v6-c-card__title-text"
                                id="card-view-basic-example-gallery-card-3-check-label"
                              >Apache Spark</h2>
                              <div class="pf-v6-c-content">
                                <small>Provided by Red Hat</small>
                              </div>
                            </div>
                            <div
                              class="pf-v6-c-card__body"
                            >This documentation page covers the Apache Spark component for the Apache Camel.</div>
                          </div>
                          <div
                            class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                            id="card-view-basic-example-gallery-card-4"
                          >
                            <div class="pf-v6-c-card__header">
                              <img
                                src="/assets/images/camel-avro_200x150.png"
                                width="60px"
                                alt="Logo"
                              />
                              <div class="pf-v6-c-card__actions">
                                <button
                                  class="pf-v6-c-menu-toggle pf-m-plain"
                                  type="button"
                                  aria-expanded="false"
                                  aria-label="Menu toggle"
                                  id="card-view-basic-example-gallery-card-4-toggle"
                                >
                                  <span class="pf-v6-c-menu-toggle__icon">
                                    <svg
                                      class="pf-v6-svg"
                                      viewBox="0 0 32 32"
                                      fill="currentColor"
                                      aria-hidden="true"
                                      role="img"
                                      width="1em"
                                      height="1em"
                                    >
                                      <path
                                        d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                      />
                                    </svg>
                                  </span>
                                </button>
                                <div class="pf-v6-c-check pf-m-standalone">
                                  <input
                                    class="pf-v6-c-check__input"
                                    type="checkbox"
                                    id="card-view-basic-example-gallery-card-4-check"
                                    name="card-view-basic-example-gallery-card-4-check"
                                    aria-labelledby="card-view-basic-example-gallery-card-4-check-label"
                                  />
                                </div>
                              </div>
                            </div>
                            <div class="pf-v6-c-card__title">
                              <h2
                                class="pf-v6-c-card__title-text"
                                id="card-view-basic-example-gallery-card-4-check-label"
                              >Avro</h2>
                              <div class="pf-v6-c-content">
                                <small>Provided by Red Hat</small>
                              </div>
                            </div>
                            <div
                              class="pf-v6-c-card__body"
                            >This component provides a dataformat for avro, which allows serialization and deserialization of messages using Apache Avro’s binary dataformat. Moreover, it provides support for Apache Avro’s rpc, by providing producers and consumers endpoint for using avro over netty or http.</div>
                          </div>
                          <div
                            class="pf-v6-c-card pf-m-selectable-raised pf-m-selected-raised pf-m-compact"
                            id="card-view-basic-example-gallery-card-5"
                          >
                            <div class="pf-v6-c-card__header">
                              <img
                                src="/assets/images/FuseConnector_Icons_AzureServices.png"
                                width="60px"
                                alt="Logo"
                              />
                              <div class="pf-v6-c-card__actions">
                                <button
                                  class="pf-v6-c-menu-toggle pf-m-plain"
                                  type="button"
                                  aria-expanded="false"
                                  aria-label="Menu toggle"
                                  id="card-view-basic-example-gallery-card-5-toggle"
                                >
                                  <span class="pf-v6-c-menu-toggle__icon">
                                    <svg
                                      class="pf-v6-svg"
                                      viewBox="0 0 32 32"
                                      fill="currentColor"
                                      aria-hidden="true"
                                      role="img"
                                      width="1em"
                                      height="1em"
                                    >
                                      <path
                                        d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                      />
                                    </svg>
                                  </span>
                                </button>
                                <div class="pf-v6-c-check pf-m-standalone">
                                  <input
                                    class="pf-v6-c-check__input"
                                    type="checkbox"
                                    id="card-view-basic-example-gallery-card-5-check"
                                    name="card-view-basic-example-gallery-card-5-check"
                                    aria-labelledby="card-view-basic-example-gallery-card-5-check-label"
                                  />
                                </div>
                              </div>
                            </div>
                            <div class="pf-v6-c-card__title">
                              <h2
                                class="pf-v6-c-card__title-text"
                                id="card-view-basic-example-gallery-card-5-check-label"
                              >Azure Services</h2>
                              <div class="pf-v6-c-content">
                                <small>Provided by Red Hat</small>
                              </div>
                            </div>
                            <div
                              class="pf-v6-c-card__body"
                            >The Camel Components for Windows Azure Services provide connectivity to Azure services from Camel.</div>
                          </div>
                          <div
                            class="pf-v6-c-card pf-m-non-selectable-raised pf-m-compact"
                            id="card-view-basic-example-gallery-card-6"
                          >
                            <div class="pf-v6-c-card__header">
                              <img
                                src="/assets/images/camel-saxon_200x150.png"
                                width="60px"
                                alt="Logo"
                              />
                              <div class="pf-v6-c-card__actions">
                                <button
                                  class="pf-v6-c-menu-toggle pf-m-plain"
                                  type="button"
                                  aria-expanded="false"
                                  aria-label="Menu toggle"
                                  id="card-view-basic-example-gallery-card-6-toggle"
                                >
                                  <span class="pf-v6-c-menu-toggle__icon">
                                    <svg
                                      class="pf-v6-svg"
                                      viewBox="0 0 32 32"
                                      fill="currentColor"
                                      aria-hidden="true"
                                      role="img"
                                      width="1em"
                                      height="1em"
                                    >
                                      <path
                                        d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                      />
                                    </svg>
                                  </span>
                                </button>
                                <div class="pf-v6-c-check pf-m-standalone">
                                  <input
                                    class="pf-v6-c-check__input"
                                    type="checkbox"
                                    id="card-view-basic-example-gallery-card-6-check"
                                    name="card-view-basic-example-gallery-card-6-check"
                                    disabled
                                    aria-labelledby="card-view-basic-example-gallery-card-6-check-label"
                                  />
                                </div>
                              </div>
                            </div>
                            <div class="pf-v6-c-card__title">
                              <h2
                                class="pf-v6-c-card__title-text"
                                id="card-view-basic-example-gallery-card-6-check-label"
                              >Crypto</h2>
                              <div class="pf-v6-c-content">
                                <small>Provided by Red Hat</small>
                              </div>
                            </div>
                            <div
                              class="pf-v6-c-card__body"
                            >For providing flexible endpoints to sign and verify exchanges using the Signature Service of the Java Cryptographic Extension.</div>
                          </div>
                          <div
                            class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                            id="card-view-basic-example-gallery-card-7"
                          >
                            <div class="pf-v6-c-card__header">
                              <img
                                src="/assets/images/camel-dropbox_200x150.png"
                                width="60px"
                                alt="Logo"
                              />
                              <div class="pf-v6-c-card__actions">
                                <button
                                  class="pf-v6-c-menu-toggle pf-m-plain"
                                  type="button"
                                  aria-expanded="false"
                                  aria-label="Menu toggle"
                                  id="card-view-basic-example-gallery-card-7-toggle"
                                >
                                  <span class="pf-v6-c-menu-toggle__icon">
                                    <svg
                                      class="pf-v6-svg"
                                      viewBox="0 0 32 32"
                                      fill="currentColor"
                                      aria-hidden="true"
                                      role="img"
                                      width="1em"
                                      height="1em"
                                    >
                                      <path
                                        d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                      />
                                    </svg>
                                  </span>
                                </button>
                                <div class="pf-v6-c-check pf-m-standalone">
                                  <input
                                    class="pf-v6-c-check__input"
                                    type="checkbox"
                                    id="card-view-basic-example-gallery-card-7-check"
                                    name="card-view-basic-example-gallery-card-7-check"
                                    aria-labelledby="card-view-basic-example-gallery-card-7-check-label"
                                  />
                                </div>
                              </div>
                            </div>
                            <div class="pf-v6-c-card__title">
                              <h2
                                class="pf-v6-c-card__title-text"
                                id="card-view-basic-example-gallery-card-7-check-label"
                              >DropBox</h2>
                              <div class="pf-v6-c-content">
                                <small>Provided by Red Hat</small>
                              </div>
                            </div>
                            <div
                              class="pf-v6-c-card__body"
                            >The dropbox: component allows you to treat Dropbox remote folders as a producer or consumer of messages.</div>
                          </div>
                          <div
                            class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                            id="card-view-basic-example-gallery-card-8"
                          >
                            <div class="pf-v6-c-card__header">
                              <img
                                src="/assets/images/camel-infinispan_200x150.png"
                                width="60px"
                                alt="Logo"
                              />
                              <div class="pf-v6-c-card__actions">
                                <button
                                  class="pf-v6-c-menu-toggle pf-m-plain"
                                  type="button"
                                  aria-expanded="false"
                                  aria-label="Menu toggle"
                                  id="card-view-basic-example-gallery-card-8-toggle"
                                >
                                  <span class="pf-v6-c-menu-toggle__icon">
                                    <svg
                                      class="pf-v6-svg"
                                      viewBox="0 0 32 32"
                                      fill="currentColor"
                                      aria-hidden="true"
                                      role="img"
                                      width="1em"
                                      height="1em"
                                    >
                                      <path
                                        d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                      />
                                    </svg>
                                  </span>
                                </button>
                                <div class="pf-v6-c-check pf-m-standalone">
                                  <input
                                    class="pf-v6-c-check__input"
                                    type="checkbox"
                                    id="card-view-basic-example-gallery-card-8-check"
                                    name="card-view-basic-example-gallery-card-8-check"
                                    aria-labelledby="card-view-basic-example-gallery-card-8-check-label"
                                  />
                                </div>
                              </div>
                            </div>
                            <div class="pf-v6-c-card__title">
                              <h2
                                class="pf-v6-c-card__title-text"
                                id="card-view-basic-example-gallery-card-8-check-label"
                              >JBoss Data Grid</h2>
                              <div class="pf-v6-c-content">
                                <small>Provided by Red Hat</small>
                              </div>
                            </div>
                            <div
                              class="pf-v6-c-card__body"
                            >Read or write to a fully-supported distributed cache and data grid for faster integration services.</div>
                          </div>
                          <div
                            class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                            id="card-view-basic-example-gallery-card-9"
                          >
                            <div class="pf-v6-c-card__header">
                              <img
                                src="/assets/images/FuseConnector_Icons_REST.png"
                                width="60px"
                                alt="Logo"
                              />
                              <div class="pf-v6-c-card__actions">
                                <button
                                  class="pf-v6-c-menu-toggle pf-m-plain"
                                  type="button"
                                  aria-expanded="false"
                                  aria-label="Menu toggle"
                                  id="card-view-basic-example-gallery-card-9-toggle"
                                >
                                  <span class="pf-v6-c-menu-toggle__icon">
                                    <svg
                                      class="pf-v6-svg"
                                      viewBox="0 0 32 32"
                                      fill="currentColor"
                                      aria-hidden="true"
                                      role="img"
                                      width="1em"
                                      height="1em"
                                    >
                                      <path
                                        d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                      />
                                    </svg>
                                  </span>
                                </button>
                                <div class="pf-v6-c-check pf-m-standalone">
                                  <input
                                    class="pf-v6-c-check__input"
                                    type="checkbox"
                                    id="card-view-basic-example-gallery-card-9-check"
                                    name="card-view-basic-example-gallery-card-9-check"
                                    aria-labelledby="card-view-basic-example-gallery-card-9-check-label"
                                  />
                                </div>
                              </div>
                            </div>
                            <div class="pf-v6-c-card__title">
                              <h2
                                class="pf-v6-c-card__title-text"
                                id="card-view-basic-example-gallery-card-9-check-label"
                              >Rest</h2>
                              <div class="pf-v6-c-content">
                                <small>Provided by Red Hat</small>
                              </div>
                            </div>
                            <div class="pf-v6-c-card__body">
                              The rest component allows to define REST endpoints (consumer) using the Rest DSL and plugin to other Camel components as the REST transport.
                              From Camel 2.18 onwards the rest component can also be used as a client (producer) to call REST services.
                            </div>
                          </div>
                          <div
                            class="pf-v6-c-card pf-m-selectable-raised pf-m-compact"
                            id="card-view-basic-example-gallery-card-10"
                          >
                            <div class="pf-v6-c-card__header">
                              <img
                                src="/assets/images/camel-swagger-java_200x150.png"
                                width="60px"
                                alt="Logo"
                              />
                              <div class="pf-v6-c-card__actions">
                                <button
                                  class="pf-v6-c-menu-toggle pf-m-plain"
                                  type="button"
                                  aria-expanded="false"
                                  aria-label="Menu toggle"
                                  id="card-view-basic-example-gallery-card-10-toggle"
                                >
                                  <span class="pf-v6-c-menu-toggle__icon">
                                    <svg
                                      class="pf-v6-svg"
                                      viewBox="0 0 32 32"
                                      fill="currentColor"
                                      aria-hidden="true"
                                      role="img"
                                      width="1em"
                                      height="1em"
                                    >
                                      <path
                                        d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                                      />
                                    </svg>
                                  </span>
                                </button>
                                <div class="pf-v6-c-check pf-m-standalone">
                                  <input
                                    class="pf-v6-c-check__input"
                                    type="checkbox"
                                    id="card-view-basic-example-gallery-card-10-check"
                                    name="card-view-basic-example-gallery-card-10-check"
                                    aria-labelledby="card-view-basic-example-gallery-card-10-check-label"
                                  />
                                </div>
                              </div>
                            </div>
                            <div class="pf-v6-c-card__title">
                              <h2
                                class="pf-v6-c-card__title-text"
                                id="card-view-basic-example-gallery-card-10-check-label"
                              >SWAGGER</h2>
                              <div class="pf-v6-c-content">
                                <small>Provided by Red Hat</small>
                              </div>
                            </div>
                            <div
                              class="pf-v6-c-card__body"
                            >Expose REST services and their APIs using Swagger specification.</div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="pf-v6-c-compass__main-footer pf-m-expanded">
                <div class="pf-v6-c-compass__message-bar">
                  <div
                    class="pf-v6-c-panel pf-m-pill pf-m-glass pf-m-no-border"
                  >
                    <div class="pf-v6-c-panel__main">chatbot message bar</div>
                  </div>
                </div>
              </div>
            </div>
            <div class="pf-v6-c-compass__sidebar pf-m-expanded pf-m-end">
              <div class="pf-v6-c-panel pf-m-pill pf-m-glass">
                <div class="pf-v6-c-panel__main">
                  <div class="pf-v6-c-panel__main-body">
                    <div class="pf-v6-c-action-list pf-m-icons pf-m-vertical">
                      <div class="pf-v6-c-action-list__item">
                        <button
                          class="pf-v6-c-button pf-m-circle pf-m-plain"
                          type="button"
                          aria-label="Notifications"
                        >
                          <span class="pf-v6-c-button__icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M28 21c-1.103 0-2-.897-2-2v-4c0-4.885-3.523-8.955-8.159-9.823.405-.445.659-1.03.659-1.677C18.5 2.122 17.379 1 16 1s-2.5 1.122-2.5 2.5c0 .647.254 1.233.659 1.677C9.523 6.045 6 10.115 6 15v4c0 1.103-.897 2-2 2a1 1 0 0 0-1 1v3.5c0 .827.673 1.5 1.5 1.5H12c0 2.206 1.794 4 4 4s4-1.794 4-4h7.5c.827 0 1.5-.673 1.5-1.5V22a1 1 0 0 0-1-1Zm-1 4H5v-2.126A4.006 4.006 0 0 0 8 19v-4c0-4.411 3.589-8 8-8s8 3.589 8 8v4a4.008 4.008 0 0 0 3 3.874V25Z"
                              />
                            </svg>
                          </span>
                        </button>
                      </div>
                      <div class="pf-v6-c-action-list__item">
                        <button
                          class="pf-v6-c-button pf-m-circle pf-m-plain"
                          type="button"
                          aria-label="List"
                        >
                          <span class="pf-v6-c-button__icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M31 16a1 1 0 0 1-1 1H9a1 1 0 0 1 0-2h21a1 1 0 0 1 1 1Zm-1 9H9a1 1 0 0 0 0 2h21a1 1 0 0 0 0-2ZM9 7h21a1 1 0 0 0 0-2H9a1 1 0 0 0 0 2ZM2 4.51a1.5 1.5 0 1 0 .001 3.001A1.5 1.5 0 0 0 2 4.51Zm0 10a1.5 1.5 0 1 0 .001 3.001A1.5 1.5 0 0 0 2 14.51Zm0 10a1.5 1.5 0 1 0 .001 3.001A1.5 1.5 0 0 0 2 24.51Z"
                              />
                            </svg>
                          </span>
                        </button>
                      </div>
                      <div class="pf-v6-c-action-list__item">
                        <button
                          class="pf-v6-c-button pf-m-circle pf-m-plain"
                          type="button"
                          aria-label="Zap"
                        >
                          <span class="pf-v6-c-button__icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M15 31a1 1 0 0 1-1-1V19h-4a.999.999 0 0 1-.916-1.401l7-16A1 1 0 0 1 18 2v11h4a.999.999 0 0 1 .916 1.401l-7 16A.998.998 0 0 1 15 31Zm-3.471-14H14.5c.827 0 1.5.673 1.5 1.5v6.719L20.471 15H17.5c-.827 0-1.5-.673-1.5-1.5V6.781L11.529 17Z"
                              />
                            </svg>
                          </span>
                        </button>
                      </div>
                      <div class="pf-v6-c-action-list__item">
                        <button
                          class="pf-v6-c-button pf-m-circle pf-m-plain"
                          type="button"
                          aria-label="Download"
                        >
                          <span class="pf-v6-c-button__icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M30 29a1 1 0 0 1-1 1H3a1 1 0 0 1 0-2h26a1 1 0 0 1 1 1Zm-15.061-4.646c.292.292.676.438 1.061.438s.768-.146 1.061-.438l8.646-8.646a.999.999 0 1 0-1.414-1.414L17 21.587V3a1 1 0 0 0-2 0v18.586l-7.293-7.293a.999.999 0 1 0-1.414 1.414l8.646 8.646Z"
                              />
                            </svg>
                          </span>
                        </button>
                      </div>
                      <div class="pf-v6-c-action-list__item">
                        <button
                          class="pf-v6-c-button pf-m-circle pf-m-plain"
                          type="button"
                          aria-label="Help"
                        >
                          <span class="pf-v6-c-button__icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                              />
                            </svg>
                          </span>
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="pf-v6-c-drawer__panel">
      <div class="pf-v6-c-drawer__head">
        <span>Drawer panel header content</span>
        <div class="pf-v6-c-drawer__actions">
          <div class="pf-v6-c-drawer__close">
            <button
              class="pf-v6-c-button pf-m-plain"
              type="button"
              aria-label="Close drawer panel"
            >
              <span class="pf-v6-c-button__icon">
                <svg
                  class="pf-v6-svg"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                  aria-hidden="true"
                  role="img"
                  width="1em"
                  height="1em"
                >
                  <path
                    d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                  />
                </svg>
              </span>
            </button>
          </div>
        </div>
      </div>
      <div
        class="pf-v6-c-drawer__description"
      >This is a helpful description of the drawer panel.</div>
      <div class="pf-v6-c-drawer__body">Drawer panel body content</div>
    </div>
  </div>
</div>

```

### Docked nav

```html isFullscreen isBeta
<div class="pf-v6-c-compass pf-m-animate-smoothly pf-m-docked">
  <div class="pf-v6-c-compass__container">
    <header class="pf-v6-c-masthead pf-m-display-inline">
      <div class="pf-v6-c-masthead__main">
        <span class="pf-v6-c-masthead__toggle">
          <button
            class="pf-v6-c-button pf-m-hamburger pf-m-plain"
            type="button"
            aria-label="Global navigation"
          >
            <span class="pf-v6-c-button__icon">
              <svg
                viewBox="0 0 10 10"
                class="pf-v6-c-button--hamburger-icon pf-v6-svg"
                width="1em"
                height="1em"
              >
                <path
                  class="pf-v6-c-button--hamburger-icon--top"
                  d="M1,1 L9,1"
                />
                <path
                  class="pf-v6-c-button--hamburger-icon--middle"
                  d="M1,5 L9,5"
                />
                <path
                  class="pf-v6-c-button--hamburger-icon--arrow"
                  d="M1,5 L1,5 L1,5"
                />
                <path
                  class="pf-v6-c-button--hamburger-icon--bottom"
                  d="M9,9 L1,9"
                />
              </svg>
            </span>
          </button>
        </span>
        <div class="pf-v6-c-masthead__brand">
          <a class="pf-v6-c-masthead__logo" href="#">
            <svg height="37px" viewBox="0 0 679 158">
              <title>PatternFly</title>
              <defs>
                <linearGradient
                  x1="68%"
                  y1="2.25860997e-13%"
                  x2="32%"
                  y2="100%"
                  id="linearGradient-"
                >
                  <stop stop-color="#2B9AF3" offset="0%" />
                  <stop
                    stop-color="#73BCF7"
                    stop-opacity="0.502212631"
                    offset="100%"
                  />
                </linearGradient>
              </defs>
              <g
                stroke="none"
                stroke-width="1"
                fill="none"
                fill-rule="evenodd"
              >
                <g
                  transform="translate(206.000000, 45.750000)"
                  fill="var(--pf-t--global--text--color--regular)"
                  fill-rule="nonzero"
                >
                  <path
                    d="M0,65.25 L0,2.25 L33.21,2.25 C37.35,2.25 41.025,3.135 44.235,4.905 C47.445,6.675 49.98,9.09 51.84,12.15 C53.7,15.21 54.63,18.72 54.63,22.68 C54.63,26.46 53.7,29.865 51.84,32.895 C49.98,35.925 47.43,38.31 44.19,40.05 C40.95,41.79 37.29,42.66 33.21,42.66 L15.48,42.66 L15.48,65.25 L0,65.25 Z M15.48,29.88 L31.41,29.88 C33.69,29.88 35.52,29.22 36.9,27.9 C38.28,26.58 38.97,24.87 38.97,22.77 C38.97,20.61 38.28,18.855 36.9,17.505 C35.52,16.155 33.69,15.48 31.41,15.48 L15.48,15.48 L15.48,29.88 Z"
                  />
                  <path
                    d="M77.04,66.06 C73.68,66.06 70.695,65.43 68.085,64.17 C65.475,62.91 63.435,61.17 61.965,58.95 C60.495,56.73 59.76,54.18 59.76,51.3 C59.76,46.74 61.485,43.215 64.935,40.725 C68.385,38.235 73.2,36.99 79.38,36.99 C83.1,36.99 86.7,37.44 90.18,38.34 L90.18,36 C90.18,31.26 87.15,28.89 81.09,28.89 C77.49,28.89 72.69,30.15 66.69,32.67 L61.47,21.96 C69.15,18.48 76.56,16.74 83.7,16.74 C90.3,16.74 95.43,18.315 99.09,21.465 C102.75,24.615 104.58,29.04 104.58,34.74 L104.58,65.25 L90.18,65.25 L90.18,62.37 C88.26,63.69 86.235,64.635 84.105,65.205 C81.975,65.775 79.62,66.06 77.04,66.06 Z M73.62,51.03 C73.62,52.53 74.28,53.7 75.6,54.54 C76.92,55.38 78.75,55.8 81.09,55.8 C84.69,55.8 87.72,55.05 90.18,53.55 L90.18,47.43 C87.42,46.71 84.54,46.35 81.54,46.35 C79.02,46.35 77.07,46.755 75.69,47.565 C74.31,48.375 73.62,49.53 73.62,51.03 Z"
                  />
                  <path
                    d="M137.25,65.88 C125.73,65.88 119.97,60.84 119.97,50.76 L119.97,29.79 L110.34,29.79 L110.34,17.64 L119.97,17.64 L119.97,5.4 L134.55,2.25 L134.55,17.64 L147.87,17.64 L147.87,29.79 L134.55,29.79 L134.55,47.88 C134.55,49.98 135.015,51.465 135.945,52.335 C136.875,53.205 138.51,53.64 140.85,53.64 C143.01,53.64 145.2,53.31 147.42,52.65 L147.42,64.44 C146.1,64.86 144.42,65.205 142.38,65.475 C140.34,65.745 138.63,65.88 137.25,65.88 Z"
                  />
                  <path
                    d="M177.57,65.88 C166.05,65.88 160.29,60.84 160.29,50.76 L160.29,29.79 L150.66,29.79 L150.66,17.64 L160.29,17.64 L160.29,5.4 L174.87,2.25 L174.87,17.64 L188.19,17.64 L188.19,29.79 L174.87,29.79 L174.87,47.88 C174.87,49.98 175.335,51.465 176.265,52.335 C177.195,53.205 178.83,53.64 181.17,53.64 C183.33,53.64 185.52,53.31 187.74,52.65 L187.74,64.44 C186.42,64.86 184.74,65.205 182.7,65.475 C180.66,65.745 178.95,65.88 177.57,65.88 Z"
                  />
                  <path
                    d="M217.62,66.15 C212.76,66.15 208.365,65.055 204.435,62.865 C200.505,60.675 197.4,57.72 195.12,54 C192.84,50.28 191.7,46.11 191.7,41.49 C191.7,36.87 192.795,32.7 194.985,28.98 C197.175,25.26 200.16,22.305 203.94,20.115 C207.72,17.925 211.92,16.83 216.54,16.83 C221.22,16.83 225.36,17.955 228.96,20.205 C232.56,22.455 235.395,25.53 237.465,29.43 C239.535,33.33 240.57,37.8 240.57,42.84 L240.57,46.44 L206.64,46.44 C207.6,48.66 209.1,50.475 211.14,51.885 C213.18,53.295 215.58,54 218.34,54 C222.42,54 225.6,52.8 227.88,50.4 L237.51,58.95 C234.51,61.47 231.435,63.3 228.285,64.44 C225.135,65.58 221.58,66.15 217.62,66.15 Z M206.37,36.27 L226.26,36.27 C225.48,33.99 224.205,32.16 222.435,30.78 C220.665,29.4 218.61,28.71 216.27,28.71 C213.87,28.71 211.8,29.37 210.06,30.69 C208.32,32.01 207.09,33.87 206.37,36.27 Z"
                  />
                  <path
                    d="M247.41,65.25 L247.41,17.64 L261.99,17.64 L261.99,22.41 C265.23,18.51 269.4,16.56 274.5,16.56 C277.08,16.62 278.91,17.01 279.99,17.73 L279.99,30.42 C277.95,29.46 275.64,28.98 273.06,28.98 C270.78,28.98 268.665,29.505 266.715,30.555 C264.765,31.605 263.19,33.09 261.99,35.01 L261.99,65.25 L247.41,65.25 Z"
                  />
                  <path
                    d="M286.29,65.25 L286.29,17.64 L300.87,17.64 L300.87,20.88 C304.47,18.12 308.73,16.74 313.65,16.74 C317.37,16.74 320.655,17.55 323.505,19.17 C326.355,20.79 328.59,23.04 330.21,25.92 C331.83,28.8 332.64,32.13 332.64,35.91 L332.64,65.25 L318.06,65.25 L318.06,37.89 C318.06,35.25 317.28,33.15 315.72,31.59 C314.16,30.03 312.06,29.25 309.42,29.25 C305.76,29.25 302.91,30.51 300.87,33.03 L300.87,65.25 L286.29,65.25 Z"
                  />
                  <polygon
                    points="342 65.25 342 2.25 392.04 2.25 392.04 15.66 357.48 15.66 357.48 27.45 380.52 27.45 380.52 40.41 357.48 40.41 357.48 65.25"
                  />
                  <polygon
                    points="399.96 65.25 399.96 2.25 414.54 0 414.54 65.25"
                  />
                  <path
                    d="M429.21,84.69 C428.07,84.69 426.96,84.645 425.88,84.555 C424.8,84.465 423.9,84.33 423.18,84.15 L423.18,71.73 C424.38,71.97 425.88,72.09 427.68,72.09 C432.36,72.09 435.51,70.05 437.13,65.97 L437.13,65.88 L418.86,17.64 L434.97,17.64 L445.5,47.61 L457.74,17.64 L473.49,17.64 L452.16,67.68 C450.42,71.82 448.5,75.135 446.4,77.625 C444.3,80.115 441.87,81.915 439.11,83.025 C436.35,84.135 433.05,84.69 429.21,84.69 Z"
                  />
                </g>
                <g transform="translate(0.000000, 0.000000)">
                  <path
                    d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                    fill="#0066CC"
                  />
                  <path
                    d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                    fill="url(#linearGradient-)"
                  />
                  <path
                    d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                    fill="url(#linearGradient-)"
                    transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                  />
                </g>
              </g>
            </svg>
          </a>
        </div>
      </div>
      <div class="pf-v6-c-masthead__content">
        <div class="pf-v6-c-toolbar pf-m-static">
          <div class="pf-v6-c-toolbar__content">
            <div class="pf-v6-c-toolbar__content-section">
              <div class="pf-v6-c-toolbar__item pf-m-align-end">
                <button
                  class="pf-v6-c-button pf-m-plain"
                  type="button"
                  aria-label="Search"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 512 512"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M505 442.7L405.3 343c-4.5-4.5-10.6-7-17-7H372c27.6-35.3 44-79.7 44-128C416 93.1 322.9 0 208 0S0 93.1 0 208s93.1 208 208 208c48.3 0 92.7-16.4 128-44v16.3c0 6.4 2.5 12.5 7 17l99.7 99.7c9.4 9.4 24.6 9.4 33.9 0l28.3-28.3c9.4-9.4 9.4-24.6.1-34zM208 336c-70.7 0-128-57.2-128-128 0-70.7 57.2-128 128-128 70.7 0 128 57.2 128 128 0 70.7-57.2 128-128 128z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
    <div class="pf-v6-c-compass__dock">
      <div class="pf-v6-c-compass__dock-main">
        <div class="pf-v6-c-skip-to-content">
          <a class="pf-v6-c-button pf-m-primary" href="#main-content-">
            <span class="pf-v6-c-button__text">Skip to content</span>
          </a>
        </div>

        <header
          class="pf-v6-c-masthead pf-m-docked"
          id="compass-docked-example-masthead"
        >
          <div class="pf-v6-c-masthead__main">
            <span class="pf-v6-c-masthead__toggle">
              <button
                class="pf-v6-c-button pf-m-hamburger pf-m-plain"
                type="button"
                aria-label="Global navigation"
              >
                <span class="pf-v6-c-button__icon">
                  <svg
                    viewBox="0 0 10 10"
                    class="pf-v6-c-button--hamburger-icon pf-v6-svg"
                    width="1em"
                    height="1em"
                  >
                    <path
                      class="pf-v6-c-button--hamburger-icon--top"
                      d="M1,1 L9,1"
                    />
                    <path
                      class="pf-v6-c-button--hamburger-icon--middle"
                      d="M1,5 L9,5"
                    />
                    <path
                      class="pf-v6-c-button--hamburger-icon--arrow"
                      d="M1,5 L1,5 L1,5"
                    />
                    <path
                      class="pf-v6-c-button--hamburger-icon--bottom"
                      d="M9,9 L1,9"
                    />
                  </svg>
                </span>
              </button>
            </span>
            <div class="pf-v6-c-masthead__brand">
              <a class="pf-v6-c-masthead__logo" href="#">
                <svg height="37px" viewBox="0 0 679 158">
                  <title>PatternFly</title>
                  <defs>
                    <linearGradient
                      x1="68%"
                      y1="2.25860997e-13%"
                      x2="32%"
                      y2="100%"
                      id="linearGradient-compass-docked-example-masthead"
                    >
                      <stop stop-color="#2B9AF3" offset="0%" />
                      <stop
                        stop-color="#73BCF7"
                        stop-opacity="0.502212631"
                        offset="100%"
                      />
                    </linearGradient>
                  </defs>
                  <g
                    stroke="none"
                    stroke-width="1"
                    fill="none"
                    fill-rule="evenodd"
                  >
                    <g
                      transform="translate(206.000000, 45.750000)"
                      fill="var(--pf-t--global--text--color--regular)"
                      fill-rule="nonzero"
                    >
                      <path
                        d="M0,65.25 L0,2.25 L33.21,2.25 C37.35,2.25 41.025,3.135 44.235,4.905 C47.445,6.675 49.98,9.09 51.84,12.15 C53.7,15.21 54.63,18.72 54.63,22.68 C54.63,26.46 53.7,29.865 51.84,32.895 C49.98,35.925 47.43,38.31 44.19,40.05 C40.95,41.79 37.29,42.66 33.21,42.66 L15.48,42.66 L15.48,65.25 L0,65.25 Z M15.48,29.88 L31.41,29.88 C33.69,29.88 35.52,29.22 36.9,27.9 C38.28,26.58 38.97,24.87 38.97,22.77 C38.97,20.61 38.28,18.855 36.9,17.505 C35.52,16.155 33.69,15.48 31.41,15.48 L15.48,15.48 L15.48,29.88 Z"
                      />
                      <path
                        d="M77.04,66.06 C73.68,66.06 70.695,65.43 68.085,64.17 C65.475,62.91 63.435,61.17 61.965,58.95 C60.495,56.73 59.76,54.18 59.76,51.3 C59.76,46.74 61.485,43.215 64.935,40.725 C68.385,38.235 73.2,36.99 79.38,36.99 C83.1,36.99 86.7,37.44 90.18,38.34 L90.18,36 C90.18,31.26 87.15,28.89 81.09,28.89 C77.49,28.89 72.69,30.15 66.69,32.67 L61.47,21.96 C69.15,18.48 76.56,16.74 83.7,16.74 C90.3,16.74 95.43,18.315 99.09,21.465 C102.75,24.615 104.58,29.04 104.58,34.74 L104.58,65.25 L90.18,65.25 L90.18,62.37 C88.26,63.69 86.235,64.635 84.105,65.205 C81.975,65.775 79.62,66.06 77.04,66.06 Z M73.62,51.03 C73.62,52.53 74.28,53.7 75.6,54.54 C76.92,55.38 78.75,55.8 81.09,55.8 C84.69,55.8 87.72,55.05 90.18,53.55 L90.18,47.43 C87.42,46.71 84.54,46.35 81.54,46.35 C79.02,46.35 77.07,46.755 75.69,47.565 C74.31,48.375 73.62,49.53 73.62,51.03 Z"
                      />
                      <path
                        d="M137.25,65.88 C125.73,65.88 119.97,60.84 119.97,50.76 L119.97,29.79 L110.34,29.79 L110.34,17.64 L119.97,17.64 L119.97,5.4 L134.55,2.25 L134.55,17.64 L147.87,17.64 L147.87,29.79 L134.55,29.79 L134.55,47.88 C134.55,49.98 135.015,51.465 135.945,52.335 C136.875,53.205 138.51,53.64 140.85,53.64 C143.01,53.64 145.2,53.31 147.42,52.65 L147.42,64.44 C146.1,64.86 144.42,65.205 142.38,65.475 C140.34,65.745 138.63,65.88 137.25,65.88 Z"
                      />
                      <path
                        d="M177.57,65.88 C166.05,65.88 160.29,60.84 160.29,50.76 L160.29,29.79 L150.66,29.79 L150.66,17.64 L160.29,17.64 L160.29,5.4 L174.87,2.25 L174.87,17.64 L188.19,17.64 L188.19,29.79 L174.87,29.79 L174.87,47.88 C174.87,49.98 175.335,51.465 176.265,52.335 C177.195,53.205 178.83,53.64 181.17,53.64 C183.33,53.64 185.52,53.31 187.74,52.65 L187.74,64.44 C186.42,64.86 184.74,65.205 182.7,65.475 C180.66,65.745 178.95,65.88 177.57,65.88 Z"
                      />
                      <path
                        d="M217.62,66.15 C212.76,66.15 208.365,65.055 204.435,62.865 C200.505,60.675 197.4,57.72 195.12,54 C192.84,50.28 191.7,46.11 191.7,41.49 C191.7,36.87 192.795,32.7 194.985,28.98 C197.175,25.26 200.16,22.305 203.94,20.115 C207.72,17.925 211.92,16.83 216.54,16.83 C221.22,16.83 225.36,17.955 228.96,20.205 C232.56,22.455 235.395,25.53 237.465,29.43 C239.535,33.33 240.57,37.8 240.57,42.84 L240.57,46.44 L206.64,46.44 C207.6,48.66 209.1,50.475 211.14,51.885 C213.18,53.295 215.58,54 218.34,54 C222.42,54 225.6,52.8 227.88,50.4 L237.51,58.95 C234.51,61.47 231.435,63.3 228.285,64.44 C225.135,65.58 221.58,66.15 217.62,66.15 Z M206.37,36.27 L226.26,36.27 C225.48,33.99 224.205,32.16 222.435,30.78 C220.665,29.4 218.61,28.71 216.27,28.71 C213.87,28.71 211.8,29.37 210.06,30.69 C208.32,32.01 207.09,33.87 206.37,36.27 Z"
                      />
                      <path
                        d="M247.41,65.25 L247.41,17.64 L261.99,17.64 L261.99,22.41 C265.23,18.51 269.4,16.56 274.5,16.56 C277.08,16.62 278.91,17.01 279.99,17.73 L279.99,30.42 C277.95,29.46 275.64,28.98 273.06,28.98 C270.78,28.98 268.665,29.505 266.715,30.555 C264.765,31.605 263.19,33.09 261.99,35.01 L261.99,65.25 L247.41,65.25 Z"
                      />
                      <path
                        d="M286.29,65.25 L286.29,17.64 L300.87,17.64 L300.87,20.88 C304.47,18.12 308.73,16.74 313.65,16.74 C317.37,16.74 320.655,17.55 323.505,19.17 C326.355,20.79 328.59,23.04 330.21,25.92 C331.83,28.8 332.64,32.13 332.64,35.91 L332.64,65.25 L318.06,65.25 L318.06,37.89 C318.06,35.25 317.28,33.15 315.72,31.59 C314.16,30.03 312.06,29.25 309.42,29.25 C305.76,29.25 302.91,30.51 300.87,33.03 L300.87,65.25 L286.29,65.25 Z"
                      />
                      <polygon
                        points="342 65.25 342 2.25 392.04 2.25 392.04 15.66 357.48 15.66 357.48 27.45 380.52 27.45 380.52 40.41 357.48 40.41 357.48 65.25"
                      />
                      <polygon
                        points="399.96 65.25 399.96 2.25 414.54 0 414.54 65.25"
                      />
                      <path
                        d="M429.21,84.69 C428.07,84.69 426.96,84.645 425.88,84.555 C424.8,84.465 423.9,84.33 423.18,84.15 L423.18,71.73 C424.38,71.97 425.88,72.09 427.68,72.09 C432.36,72.09 435.51,70.05 437.13,65.97 L437.13,65.88 L418.86,17.64 L434.97,17.64 L445.5,47.61 L457.74,17.64 L473.49,17.64 L452.16,67.68 C450.42,71.82 448.5,75.135 446.4,77.625 C444.3,80.115 441.87,81.915 439.11,83.025 C436.35,84.135 433.05,84.69 429.21,84.69 Z"
                      />
                    </g>
                    <g transform="translate(0.000000, 0.000000)">
                      <path
                        d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                        fill="#0066CC"
                      />
                      <path
                        d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                        fill="url(#linearGradient-compass-docked-example-masthead)"
                      />
                      <path
                        d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                        fill="url(#linearGradient-compass-docked-example-masthead)"
                        transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                      />
                    </g>
                  </g>
                </svg>
              </a>
              <a class="pf-v6-c-masthead__logo pf-m-compact" href="#">
                <svg width="37px" height="37px" viewBox="0 0 158 158">
                  <title>PatternFly</title>
                  <defs>
                    <linearGradient
                      x1="68%"
                      y1="2.25860997e-13%"
                      x2="32%"
                      y2="100%"
                      id="linearGradient-1"
                    >
                      <stop stop-color="#2B9AF3" offset="0%" />
                      <stop
                        stop-color="#73BCF7"
                        stop-opacity="0.502212631"
                        offset="100%"
                      />
                    </linearGradient>
                  </defs>
                  <g
                    id="PF-IconLogo-color"
                    stroke="none"
                    stroke-width="1"
                    fill="none"
                    fill-rule="evenodd"
                  >
                    <g id="Logo">
                      <path
                        d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                        id="Rectangle-Copy-17"
                        fill="#0066CC"
                      />
                      <path
                        d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                        id="Path-2"
                        fill="url(#linearGradient-1)"
                      />
                      <path
                        d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                        id="Path-2"
                        fill="url(#linearGradient-1)"
                        transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                      />
                    </g>
                  </g>
                </svg>
              </a>
            </div>
          </div>
          <hr class="pf-v6-c-divider" />
          <div class="pf-v6-c-masthead__content">
            <div
              class="pf-v6-c-toolbar pf-m-vertical pf-m-static"
              id="compass-docked-example-masthead-toolbar"
            >
              <div class="pf-v6-c-toolbar__content">
                <div class="pf-v6-c-toolbar__content-section">
                  <nav class="pf-v6-c-nav pf-m-docked" aria-label="Global">
                    <ul class="pf-v6-c-nav__list" role="list">
                      <li class="pf-v6-c-nav__item">
                        <a
                          href="#"
                          class="pf-v6-c-nav__link"
                          aria-label="Cubes"
                        >
                          <span class="pf-v6-c-nav__link-icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M12.5 12h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5v7c0 .827.673 1.5 1.5 1.5Zm.5-8h6v6h-6V4ZM5.5 25h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5v7c0 .827.673 1.5 1.5 1.5Zm.5-8h6v6H6v-6Zm24 12a1 1 0 0 1-1 1H3a1 1 0 0 1 0-2h26a1 1 0 0 1 1 1ZM18 16.5v7c0 .827.673 1.5 1.5 1.5h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5Zm2 .5h6v6h-6v-6Z"
                              />
                            </svg>
                          </span>
                          <span class="pf-v6-c-nav__link-text">System panel</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-nav__item">
                        <a
                          href="#"
                          class="pf-v6-c-nav__link pf-m-current"
                          aria-current="page"
                          aria-label="Folder"
                        >
                          <span class="pf-v6-c-nav__link-icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M29.5 8H17.81l-.681-3.208A1 1 0 0 0 16.15 4h-9.3a1 1 0 0 0-.979.792L5.19 8H2.5C1.673 8 1 8.673 1 9.5v17c0 .827.673 1.5 1.5 1.5h27c.827 0 1.5-.673 1.5-1.5v-17c0-.827-.673-1.5-1.5-1.5ZM29 26H3V10h3a1 1 0 0 0 .979-.792L7.66 6h7.682l.681 3.208a1 1 0 0 0 .979.792h12v16Z"
                              />
                            </svg>
                          </span>
                          <span class="pf-v6-c-nav__link-text">Policy</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-nav__item">
                        <a
                          href="#"
                          class="pf-v6-c-nav__link"
                          aria-label="Cloud"
                        >
                          <span class="pf-v6-c-nav__link-icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M26.996 14.228c.003-.077.004-.153.004-.228 0-4.962-4.037-9-9-9-3.899 0-7.333 2.532-8.54 6.156A6.891 6.891 0 0 0 8 11c-3.859 0-7 3.14-7 7s3.141 7 7 7h17.5c3.032 0 5.5-2.467 5.5-5.5a5.456 5.456 0 0 0-4.004-5.272ZM25.5 23H8c-2.757 0-5-2.243-5-5s2.243-5 5-5a4.97 4.97 0 0 1 1.799.34 1.003 1.003 0 0 0 1.341-.735C11.796 9.357 14.682 7 18 7c3.859 0 7 3.14 7 7 0 .311-.028.615-.067.916a1.004 1.004 0 0 0 .898 1.123 3.473 3.473 0 0 1 3.17 3.461c0 1.93-1.57 3.5-3.5 3.5Z"
                              />
                            </svg>
                          </span>
                          <span class="pf-v6-c-nav__link-text">Authentication</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-nav__item">
                        <a href="#" class="pf-v6-c-nav__link" aria-label="Code">
                          <span class="pf-v6-c-nav__link-icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M9.707 9.707 3.414 16l6.293 6.293a.999.999 0 1 1-1.414 1.414l-6.646-6.646a1.501 1.501 0 0 1 0-2.121l6.646-6.646a.999.999 0 1 1 1.414 1.414Zm20.647 5.232-6.646-6.646a.999.999 0 1 0-1.414 1.414L28.587 16l-6.293 6.293a.999.999 0 1 0 1.414 1.414l6.646-6.646a1.501 1.501 0 0 0 0-2.121ZM18.121 6.022a.997.997 0 0 0-1.186.77l-3.826 18a1 1 0 1 0 1.956.416l3.826-18a1 1 0 0 0-.77-1.186Z"
                              />
                            </svg>
                          </span>
                          <span class="pf-v6-c-nav__link-text">Network services</span>
                        </a>
                      </li>
                    </ul>
                  </nav>

                  <div
                    class="pf-v6-c-toolbar__group pf-m-align-end pf-m-spacer-none pf-m-spacer-md-on-md pf-m-action-group-plain"
                  >
                    <div class="pf-v6-c-toolbar__item">
                      <button
                        class="pf-v6-c-menu-toggle pf-m-docked pf-m-text pf-m-plain"
                        type="button"
                        aria-expanded="false"
                        aria-label="Applications"
                      >
                        <span class="pf-v6-c-menu-toggle__icon">
                          <svg
                            class="pf-v6-svg"
                            viewBox="0 0 32 32"
                            fill="currentColor"
                            aria-hidden="true"
                            role="img"
                            width="1em"
                            height="1em"
                          >
                            <path
                              d="M13.75 2H3.25C2.561 2 2 2.561 2 3.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25V3.25C15 2.561 14.439 2 13.75 2ZM13 13H4V4h9v9ZM28.75 2h-10.5C17.561 2 17 2.561 17 3.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25V3.25C30 2.561 29.439 2 28.75 2ZM28 13h-9V4h9v9Zm-14.25 4H3.25C2.561 17 2 17.561 2 18.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25v-10.5c0-.689-.561-1.25-1.25-1.25ZM13 28H4v-9h9v9Zm15.75-11h-10.5c-.689 0-1.25.561-1.25 1.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25v-10.5c0-.689-.561-1.25-1.25-1.25ZM28 28h-9v-9h9v9Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-menu-toggle__text">Applications</span>
                      </button>
                    </div>
                    <div class="pf-v6-c-toolbar__item">
                      <button
                        class="pf-v6-c-button pf-m-docked pf-m-settings pf-m-plain"
                        type="button"
                        aria-label="Settings"
                      >
                        <span class="pf-v6-c-button__icon pf-m-start">
                          <svg
                            class="pf-v6-svg"
                            viewBox="0 0 32 32"
                            fill="currentColor"
                            aria-hidden="true"
                            role="img"
                            width="1em"
                            height="1em"
                          >
                            <path
                              d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-button__text">Settings</span>
                      </button>
                    </div>
                    <div class="pf-v6-c-toolbar__item">
                      <button
                        class="pf-v6-c-menu-toggle pf-m-docked pf-m-text pf-m-plain"
                        type="button"
                        aria-expanded="false"
                        aria-label="Help"
                      >
                        <span class="pf-v6-c-menu-toggle__icon">
                          <svg
                            class="pf-v6-svg"
                            viewBox="0 0 32 32"
                            fill="currentColor"
                            aria-hidden="true"
                            role="img"
                            width="1em"
                            height="1em"
                          >
                            <path
                              d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-menu-toggle__text">Help</span>
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </header>
      </div>
    </div>
    <div class="pf-v6-c-compass__main">
      <div class="pf-v6-c-compass__main-header">
        <div class="pf-v6-c-panel pf-m-glass">
          <div class="pf-v6-c-panel__main">
            <div class="pf-v6-c-panel__main-body">
              <div class="pf-v6-c-compass__main-header-content">
                <div class="pf-v6-c-compass__main-header-title">
                  <h2 class="pf-v6-c-title pf-m-h1">Header</h2>
                </div>
                <div class="pf-v6-c-compass__main-header-toolbar">
                  <div class="pf-v6-c-action-list">
                    <div class="pf-v6-c-action-list__group">
                      <div class="pf-v6-c-action-list__item">
                        <button
                          class="pf-v6-c-button pf-m-primary"
                          type="button"
                        >
                          <span class="pf-v6-c-button__text">action</span>
                        </button>
                      </div>
                      <div class="pf-v6-c-action-list__item">
                        <button
                          class="pf-v6-c-button pf-m-secondary"
                          type="button"
                        >
                          <span class="pf-v6-c-button__text">action</span>
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-compass__content">
        <div
          class="pf-v6-c-panel pf-m-glass pf-m-scrollable-auto-height pf-m-scrollable"
        >
          <div class="pf-v6-c-panel__main">
            <div class="pf-v6-c-panel__main-body">[so much room for activities]</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

```

### Docked nav - expanded on mobile

```html isFullscreen isBeta
<div class="pf-v6-c-compass pf-m-animate-smoothly pf-m-docked">
  <div class="pf-v6-c-compass__container">
    <header class="pf-v6-c-masthead pf-m-display-inline">
      <div class="pf-v6-c-masthead__main">
        <span class="pf-v6-c-masthead__toggle">
          <button
            class="pf-v6-c-button pf-m-hamburger pf-m-plain"
            type="button"
            aria-label="Global navigation"
          >
            <span class="pf-v6-c-button__icon">
              <svg
                viewBox="0 0 10 10"
                class="pf-v6-c-button--hamburger-icon pf-v6-svg"
                width="1em"
                height="1em"
              >
                <path
                  class="pf-v6-c-button--hamburger-icon--top"
                  d="M1,1 L9,1"
                />
                <path
                  class="pf-v6-c-button--hamburger-icon--middle"
                  d="M1,5 L9,5"
                />
                <path
                  class="pf-v6-c-button--hamburger-icon--arrow"
                  d="M1,5 L1,5 L1,5"
                />
                <path
                  class="pf-v6-c-button--hamburger-icon--bottom"
                  d="M9,9 L1,9"
                />
              </svg>
            </span>
          </button>
        </span>
        <div class="pf-v6-c-masthead__brand">
          <a class="pf-v6-c-masthead__logo" href="#">
            <svg height="37px" viewBox="0 0 679 158">
              <title>PatternFly</title>
              <defs>
                <linearGradient
                  x1="68%"
                  y1="2.25860997e-13%"
                  x2="32%"
                  y2="100%"
                  id="linearGradient-"
                >
                  <stop stop-color="#2B9AF3" offset="0%" />
                  <stop
                    stop-color="#73BCF7"
                    stop-opacity="0.502212631"
                    offset="100%"
                  />
                </linearGradient>
              </defs>
              <g
                stroke="none"
                stroke-width="1"
                fill="none"
                fill-rule="evenodd"
              >
                <g
                  transform="translate(206.000000, 45.750000)"
                  fill="var(--pf-t--global--text--color--regular)"
                  fill-rule="nonzero"
                >
                  <path
                    d="M0,65.25 L0,2.25 L33.21,2.25 C37.35,2.25 41.025,3.135 44.235,4.905 C47.445,6.675 49.98,9.09 51.84,12.15 C53.7,15.21 54.63,18.72 54.63,22.68 C54.63,26.46 53.7,29.865 51.84,32.895 C49.98,35.925 47.43,38.31 44.19,40.05 C40.95,41.79 37.29,42.66 33.21,42.66 L15.48,42.66 L15.48,65.25 L0,65.25 Z M15.48,29.88 L31.41,29.88 C33.69,29.88 35.52,29.22 36.9,27.9 C38.28,26.58 38.97,24.87 38.97,22.77 C38.97,20.61 38.28,18.855 36.9,17.505 C35.52,16.155 33.69,15.48 31.41,15.48 L15.48,15.48 L15.48,29.88 Z"
                  />
                  <path
                    d="M77.04,66.06 C73.68,66.06 70.695,65.43 68.085,64.17 C65.475,62.91 63.435,61.17 61.965,58.95 C60.495,56.73 59.76,54.18 59.76,51.3 C59.76,46.74 61.485,43.215 64.935,40.725 C68.385,38.235 73.2,36.99 79.38,36.99 C83.1,36.99 86.7,37.44 90.18,38.34 L90.18,36 C90.18,31.26 87.15,28.89 81.09,28.89 C77.49,28.89 72.69,30.15 66.69,32.67 L61.47,21.96 C69.15,18.48 76.56,16.74 83.7,16.74 C90.3,16.74 95.43,18.315 99.09,21.465 C102.75,24.615 104.58,29.04 104.58,34.74 L104.58,65.25 L90.18,65.25 L90.18,62.37 C88.26,63.69 86.235,64.635 84.105,65.205 C81.975,65.775 79.62,66.06 77.04,66.06 Z M73.62,51.03 C73.62,52.53 74.28,53.7 75.6,54.54 C76.92,55.38 78.75,55.8 81.09,55.8 C84.69,55.8 87.72,55.05 90.18,53.55 L90.18,47.43 C87.42,46.71 84.54,46.35 81.54,46.35 C79.02,46.35 77.07,46.755 75.69,47.565 C74.31,48.375 73.62,49.53 73.62,51.03 Z"
                  />
                  <path
                    d="M137.25,65.88 C125.73,65.88 119.97,60.84 119.97,50.76 L119.97,29.79 L110.34,29.79 L110.34,17.64 L119.97,17.64 L119.97,5.4 L134.55,2.25 L134.55,17.64 L147.87,17.64 L147.87,29.79 L134.55,29.79 L134.55,47.88 C134.55,49.98 135.015,51.465 135.945,52.335 C136.875,53.205 138.51,53.64 140.85,53.64 C143.01,53.64 145.2,53.31 147.42,52.65 L147.42,64.44 C146.1,64.86 144.42,65.205 142.38,65.475 C140.34,65.745 138.63,65.88 137.25,65.88 Z"
                  />
                  <path
                    d="M177.57,65.88 C166.05,65.88 160.29,60.84 160.29,50.76 L160.29,29.79 L150.66,29.79 L150.66,17.64 L160.29,17.64 L160.29,5.4 L174.87,2.25 L174.87,17.64 L188.19,17.64 L188.19,29.79 L174.87,29.79 L174.87,47.88 C174.87,49.98 175.335,51.465 176.265,52.335 C177.195,53.205 178.83,53.64 181.17,53.64 C183.33,53.64 185.52,53.31 187.74,52.65 L187.74,64.44 C186.42,64.86 184.74,65.205 182.7,65.475 C180.66,65.745 178.95,65.88 177.57,65.88 Z"
                  />
                  <path
                    d="M217.62,66.15 C212.76,66.15 208.365,65.055 204.435,62.865 C200.505,60.675 197.4,57.72 195.12,54 C192.84,50.28 191.7,46.11 191.7,41.49 C191.7,36.87 192.795,32.7 194.985,28.98 C197.175,25.26 200.16,22.305 203.94,20.115 C207.72,17.925 211.92,16.83 216.54,16.83 C221.22,16.83 225.36,17.955 228.96,20.205 C232.56,22.455 235.395,25.53 237.465,29.43 C239.535,33.33 240.57,37.8 240.57,42.84 L240.57,46.44 L206.64,46.44 C207.6,48.66 209.1,50.475 211.14,51.885 C213.18,53.295 215.58,54 218.34,54 C222.42,54 225.6,52.8 227.88,50.4 L237.51,58.95 C234.51,61.47 231.435,63.3 228.285,64.44 C225.135,65.58 221.58,66.15 217.62,66.15 Z M206.37,36.27 L226.26,36.27 C225.48,33.99 224.205,32.16 222.435,30.78 C220.665,29.4 218.61,28.71 216.27,28.71 C213.87,28.71 211.8,29.37 210.06,30.69 C208.32,32.01 207.09,33.87 206.37,36.27 Z"
                  />
                  <path
                    d="M247.41,65.25 L247.41,17.64 L261.99,17.64 L261.99,22.41 C265.23,18.51 269.4,16.56 274.5,16.56 C277.08,16.62 278.91,17.01 279.99,17.73 L279.99,30.42 C277.95,29.46 275.64,28.98 273.06,28.98 C270.78,28.98 268.665,29.505 266.715,30.555 C264.765,31.605 263.19,33.09 261.99,35.01 L261.99,65.25 L247.41,65.25 Z"
                  />
                  <path
                    d="M286.29,65.25 L286.29,17.64 L300.87,17.64 L300.87,20.88 C304.47,18.12 308.73,16.74 313.65,16.74 C317.37,16.74 320.655,17.55 323.505,19.17 C326.355,20.79 328.59,23.04 330.21,25.92 C331.83,28.8 332.64,32.13 332.64,35.91 L332.64,65.25 L318.06,65.25 L318.06,37.89 C318.06,35.25 317.28,33.15 315.72,31.59 C314.16,30.03 312.06,29.25 309.42,29.25 C305.76,29.25 302.91,30.51 300.87,33.03 L300.87,65.25 L286.29,65.25 Z"
                  />
                  <polygon
                    points="342 65.25 342 2.25 392.04 2.25 392.04 15.66 357.48 15.66 357.48 27.45 380.52 27.45 380.52 40.41 357.48 40.41 357.48 65.25"
                  />
                  <polygon
                    points="399.96 65.25 399.96 2.25 414.54 0 414.54 65.25"
                  />
                  <path
                    d="M429.21,84.69 C428.07,84.69 426.96,84.645 425.88,84.555 C424.8,84.465 423.9,84.33 423.18,84.15 L423.18,71.73 C424.38,71.97 425.88,72.09 427.68,72.09 C432.36,72.09 435.51,70.05 437.13,65.97 L437.13,65.88 L418.86,17.64 L434.97,17.64 L445.5,47.61 L457.74,17.64 L473.49,17.64 L452.16,67.68 C450.42,71.82 448.5,75.135 446.4,77.625 C444.3,80.115 441.87,81.915 439.11,83.025 C436.35,84.135 433.05,84.69 429.21,84.69 Z"
                  />
                </g>
                <g transform="translate(0.000000, 0.000000)">
                  <path
                    d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                    fill="#0066CC"
                  />
                  <path
                    d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                    fill="url(#linearGradient-)"
                  />
                  <path
                    d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                    fill="url(#linearGradient-)"
                    transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                  />
                </g>
              </g>
            </svg>
          </a>
        </div>
      </div>
      <div class="pf-v6-c-masthead__content">
        <div class="pf-v6-c-toolbar pf-m-static">
          <div class="pf-v6-c-toolbar__content">
            <div class="pf-v6-c-toolbar__content-section">
              <div class="pf-v6-c-toolbar__item pf-m-align-end">
                <button
                  class="pf-v6-c-button pf-m-plain"
                  type="button"
                  aria-label="Search"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 512 512"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M505 442.7L405.3 343c-4.5-4.5-10.6-7-17-7H372c27.6-35.3 44-79.7 44-128C416 93.1 322.9 0 208 0S0 93.1 0 208s93.1 208 208 208c48.3 0 92.7-16.4 128-44v16.3c0 6.4 2.5 12.5 7 17l99.7 99.7c9.4 9.4 24.6 9.4 33.9 0l28.3-28.3c9.4-9.4 9.4-24.6.1-34zM208 336c-70.7 0-128-57.2-128-128 0-70.7 57.2-128 128-128 70.7 0 128 57.2 128 128 0 70.7-57.2 128-128 128z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
    <div class="pf-v6-c-compass__dock pf-m-expanded">
      <div class="pf-v6-c-compass__dock-main">
        <div class="pf-v6-c-skip-to-content">
          <a class="pf-v6-c-button pf-m-primary" href="#main-content-">
            <span class="pf-v6-c-button__text">Skip to content</span>
          </a>
        </div>

        <header
          class="pf-v6-c-masthead pf-m-docked"
          id="compass-docked-mobile-expanded-example-masthead"
        >
          <div class="pf-v6-c-masthead__main">
            <span class="pf-v6-c-masthead__toggle">
              <button
                class="pf-v6-c-button pf-m-hamburger pf-m-plain"
                type="button"
                aria-label="Global navigation"
              >
                <span class="pf-v6-c-button__icon">
                  <svg
                    viewBox="0 0 10 10"
                    class="pf-v6-c-button--hamburger-icon pf-v6-svg"
                    width="1em"
                    height="1em"
                  >
                    <path
                      class="pf-v6-c-button--hamburger-icon--top"
                      d="M1,1 L9,1"
                    />
                    <path
                      class="pf-v6-c-button--hamburger-icon--middle"
                      d="M1,5 L9,5"
                    />
                    <path
                      class="pf-v6-c-button--hamburger-icon--arrow"
                      d="M1,5 L1,5 L1,5"
                    />
                    <path
                      class="pf-v6-c-button--hamburger-icon--bottom"
                      d="M9,9 L1,9"
                    />
                  </svg>
                </span>
              </button>
            </span>
            <div class="pf-v6-c-masthead__brand">
              <a class="pf-v6-c-masthead__logo" href="#">
                <svg height="37px" viewBox="0 0 679 158">
                  <title>PatternFly</title>
                  <defs>
                    <linearGradient
                      x1="68%"
                      y1="2.25860997e-13%"
                      x2="32%"
                      y2="100%"
                      id="linearGradient-compass-docked-mobile-expanded-example-masthead"
                    >
                      <stop stop-color="#2B9AF3" offset="0%" />
                      <stop
                        stop-color="#73BCF7"
                        stop-opacity="0.502212631"
                        offset="100%"
                      />
                    </linearGradient>
                  </defs>
                  <g
                    stroke="none"
                    stroke-width="1"
                    fill="none"
                    fill-rule="evenodd"
                  >
                    <g
                      transform="translate(206.000000, 45.750000)"
                      fill="var(--pf-t--global--text--color--regular)"
                      fill-rule="nonzero"
                    >
                      <path
                        d="M0,65.25 L0,2.25 L33.21,2.25 C37.35,2.25 41.025,3.135 44.235,4.905 C47.445,6.675 49.98,9.09 51.84,12.15 C53.7,15.21 54.63,18.72 54.63,22.68 C54.63,26.46 53.7,29.865 51.84,32.895 C49.98,35.925 47.43,38.31 44.19,40.05 C40.95,41.79 37.29,42.66 33.21,42.66 L15.48,42.66 L15.48,65.25 L0,65.25 Z M15.48,29.88 L31.41,29.88 C33.69,29.88 35.52,29.22 36.9,27.9 C38.28,26.58 38.97,24.87 38.97,22.77 C38.97,20.61 38.28,18.855 36.9,17.505 C35.52,16.155 33.69,15.48 31.41,15.48 L15.48,15.48 L15.48,29.88 Z"
                      />
                      <path
                        d="M77.04,66.06 C73.68,66.06 70.695,65.43 68.085,64.17 C65.475,62.91 63.435,61.17 61.965,58.95 C60.495,56.73 59.76,54.18 59.76,51.3 C59.76,46.74 61.485,43.215 64.935,40.725 C68.385,38.235 73.2,36.99 79.38,36.99 C83.1,36.99 86.7,37.44 90.18,38.34 L90.18,36 C90.18,31.26 87.15,28.89 81.09,28.89 C77.49,28.89 72.69,30.15 66.69,32.67 L61.47,21.96 C69.15,18.48 76.56,16.74 83.7,16.74 C90.3,16.74 95.43,18.315 99.09,21.465 C102.75,24.615 104.58,29.04 104.58,34.74 L104.58,65.25 L90.18,65.25 L90.18,62.37 C88.26,63.69 86.235,64.635 84.105,65.205 C81.975,65.775 79.62,66.06 77.04,66.06 Z M73.62,51.03 C73.62,52.53 74.28,53.7 75.6,54.54 C76.92,55.38 78.75,55.8 81.09,55.8 C84.69,55.8 87.72,55.05 90.18,53.55 L90.18,47.43 C87.42,46.71 84.54,46.35 81.54,46.35 C79.02,46.35 77.07,46.755 75.69,47.565 C74.31,48.375 73.62,49.53 73.62,51.03 Z"
                      />
                      <path
                        d="M137.25,65.88 C125.73,65.88 119.97,60.84 119.97,50.76 L119.97,29.79 L110.34,29.79 L110.34,17.64 L119.97,17.64 L119.97,5.4 L134.55,2.25 L134.55,17.64 L147.87,17.64 L147.87,29.79 L134.55,29.79 L134.55,47.88 C134.55,49.98 135.015,51.465 135.945,52.335 C136.875,53.205 138.51,53.64 140.85,53.64 C143.01,53.64 145.2,53.31 147.42,52.65 L147.42,64.44 C146.1,64.86 144.42,65.205 142.38,65.475 C140.34,65.745 138.63,65.88 137.25,65.88 Z"
                      />
                      <path
                        d="M177.57,65.88 C166.05,65.88 160.29,60.84 160.29,50.76 L160.29,29.79 L150.66,29.79 L150.66,17.64 L160.29,17.64 L160.29,5.4 L174.87,2.25 L174.87,17.64 L188.19,17.64 L188.19,29.79 L174.87,29.79 L174.87,47.88 C174.87,49.98 175.335,51.465 176.265,52.335 C177.195,53.205 178.83,53.64 181.17,53.64 C183.33,53.64 185.52,53.31 187.74,52.65 L187.74,64.44 C186.42,64.86 184.74,65.205 182.7,65.475 C180.66,65.745 178.95,65.88 177.57,65.88 Z"
                      />
                      <path
                        d="M217.62,66.15 C212.76,66.15 208.365,65.055 204.435,62.865 C200.505,60.675 197.4,57.72 195.12,54 C192.84,50.28 191.7,46.11 191.7,41.49 C191.7,36.87 192.795,32.7 194.985,28.98 C197.175,25.26 200.16,22.305 203.94,20.115 C207.72,17.925 211.92,16.83 216.54,16.83 C221.22,16.83 225.36,17.955 228.96,20.205 C232.56,22.455 235.395,25.53 237.465,29.43 C239.535,33.33 240.57,37.8 240.57,42.84 L240.57,46.44 L206.64,46.44 C207.6,48.66 209.1,50.475 211.14,51.885 C213.18,53.295 215.58,54 218.34,54 C222.42,54 225.6,52.8 227.88,50.4 L237.51,58.95 C234.51,61.47 231.435,63.3 228.285,64.44 C225.135,65.58 221.58,66.15 217.62,66.15 Z M206.37,36.27 L226.26,36.27 C225.48,33.99 224.205,32.16 222.435,30.78 C220.665,29.4 218.61,28.71 216.27,28.71 C213.87,28.71 211.8,29.37 210.06,30.69 C208.32,32.01 207.09,33.87 206.37,36.27 Z"
                      />
                      <path
                        d="M247.41,65.25 L247.41,17.64 L261.99,17.64 L261.99,22.41 C265.23,18.51 269.4,16.56 274.5,16.56 C277.08,16.62 278.91,17.01 279.99,17.73 L279.99,30.42 C277.95,29.46 275.64,28.98 273.06,28.98 C270.78,28.98 268.665,29.505 266.715,30.555 C264.765,31.605 263.19,33.09 261.99,35.01 L261.99,65.25 L247.41,65.25 Z"
                      />
                      <path
                        d="M286.29,65.25 L286.29,17.64 L300.87,17.64 L300.87,20.88 C304.47,18.12 308.73,16.74 313.65,16.74 C317.37,16.74 320.655,17.55 323.505,19.17 C326.355,20.79 328.59,23.04 330.21,25.92 C331.83,28.8 332.64,32.13 332.64,35.91 L332.64,65.25 L318.06,65.25 L318.06,37.89 C318.06,35.25 317.28,33.15 315.72,31.59 C314.16,30.03 312.06,29.25 309.42,29.25 C305.76,29.25 302.91,30.51 300.87,33.03 L300.87,65.25 L286.29,65.25 Z"
                      />
                      <polygon
                        points="342 65.25 342 2.25 392.04 2.25 392.04 15.66 357.48 15.66 357.48 27.45 380.52 27.45 380.52 40.41 357.48 40.41 357.48 65.25"
                      />
                      <polygon
                        points="399.96 65.25 399.96 2.25 414.54 0 414.54 65.25"
                      />
                      <path
                        d="M429.21,84.69 C428.07,84.69 426.96,84.645 425.88,84.555 C424.8,84.465 423.9,84.33 423.18,84.15 L423.18,71.73 C424.38,71.97 425.88,72.09 427.68,72.09 C432.36,72.09 435.51,70.05 437.13,65.97 L437.13,65.88 L418.86,17.64 L434.97,17.64 L445.5,47.61 L457.74,17.64 L473.49,17.64 L452.16,67.68 C450.42,71.82 448.5,75.135 446.4,77.625 C444.3,80.115 441.87,81.915 439.11,83.025 C436.35,84.135 433.05,84.69 429.21,84.69 Z"
                      />
                    </g>
                    <g transform="translate(0.000000, 0.000000)">
                      <path
                        d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                        fill="#0066CC"
                      />
                      <path
                        d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                        fill="url(#linearGradient-compass-docked-mobile-expanded-example-masthead)"
                      />
                      <path
                        d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                        fill="url(#linearGradient-compass-docked-mobile-expanded-example-masthead)"
                        transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                      />
                    </g>
                  </g>
                </svg>
              </a>
              <a class="pf-v6-c-masthead__logo pf-m-compact" href="#">
                <svg width="37px" height="37px" viewBox="0 0 158 158">
                  <title>PatternFly</title>
                  <defs>
                    <linearGradient
                      x1="68%"
                      y1="2.25860997e-13%"
                      x2="32%"
                      y2="100%"
                      id="linearGradient-1"
                    >
                      <stop stop-color="#2B9AF3" offset="0%" />
                      <stop
                        stop-color="#73BCF7"
                        stop-opacity="0.502212631"
                        offset="100%"
                      />
                    </linearGradient>
                  </defs>
                  <g
                    id="PF-IconLogo-color"
                    stroke="none"
                    stroke-width="1"
                    fill="none"
                    fill-rule="evenodd"
                  >
                    <g id="Logo">
                      <path
                        d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                        id="Rectangle-Copy-17"
                        fill="#0066CC"
                      />
                      <path
                        d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                        id="Path-2"
                        fill="url(#linearGradient-1)"
                      />
                      <path
                        d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                        id="Path-2"
                        fill="url(#linearGradient-1)"
                        transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                      />
                    </g>
                  </g>
                </svg>
              </a>
            </div>
          </div>
          <hr class="pf-v6-c-divider" />
          <div class="pf-v6-c-masthead__content">
            <div
              class="pf-v6-c-toolbar pf-m-vertical pf-m-static"
              id="compass-docked-mobile-expanded-example-masthead-toolbar"
            >
              <div class="pf-v6-c-toolbar__content">
                <div class="pf-v6-c-toolbar__content-section">
                  <nav class="pf-v6-c-nav pf-m-docked" aria-label="Global">
                    <ul class="pf-v6-c-nav__list" role="list">
                      <li class="pf-v6-c-nav__item">
                        <a
                          href="#"
                          class="pf-v6-c-nav__link"
                          aria-label="Cubes"
                        >
                          <span class="pf-v6-c-nav__link-icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M12.5 12h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5v7c0 .827.673 1.5 1.5 1.5Zm.5-8h6v6h-6V4ZM5.5 25h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5v7c0 .827.673 1.5 1.5 1.5Zm.5-8h6v6H6v-6Zm24 12a1 1 0 0 1-1 1H3a1 1 0 0 1 0-2h26a1 1 0 0 1 1 1ZM18 16.5v7c0 .827.673 1.5 1.5 1.5h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5Zm2 .5h6v6h-6v-6Z"
                              />
                            </svg>
                          </span>
                          <span class="pf-v6-c-nav__link-text">System panel</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-nav__item">
                        <a
                          href="#"
                          class="pf-v6-c-nav__link pf-m-current"
                          aria-current="page"
                          aria-label="Folder"
                        >
                          <span class="pf-v6-c-nav__link-icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M29.5 8H17.81l-.681-3.208A1 1 0 0 0 16.15 4h-9.3a1 1 0 0 0-.979.792L5.19 8H2.5C1.673 8 1 8.673 1 9.5v17c0 .827.673 1.5 1.5 1.5h27c.827 0 1.5-.673 1.5-1.5v-17c0-.827-.673-1.5-1.5-1.5ZM29 26H3V10h3a1 1 0 0 0 .979-.792L7.66 6h7.682l.681 3.208a1 1 0 0 0 .979.792h12v16Z"
                              />
                            </svg>
                          </span>
                          <span class="pf-v6-c-nav__link-text">Policy</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-nav__item">
                        <a
                          href="#"
                          class="pf-v6-c-nav__link"
                          aria-label="Cloud"
                        >
                          <span class="pf-v6-c-nav__link-icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M26.996 14.228c.003-.077.004-.153.004-.228 0-4.962-4.037-9-9-9-3.899 0-7.333 2.532-8.54 6.156A6.891 6.891 0 0 0 8 11c-3.859 0-7 3.14-7 7s3.141 7 7 7h17.5c3.032 0 5.5-2.467 5.5-5.5a5.456 5.456 0 0 0-4.004-5.272ZM25.5 23H8c-2.757 0-5-2.243-5-5s2.243-5 5-5a4.97 4.97 0 0 1 1.799.34 1.003 1.003 0 0 0 1.341-.735C11.796 9.357 14.682 7 18 7c3.859 0 7 3.14 7 7 0 .311-.028.615-.067.916a1.004 1.004 0 0 0 .898 1.123 3.473 3.473 0 0 1 3.17 3.461c0 1.93-1.57 3.5-3.5 3.5Z"
                              />
                            </svg>
                          </span>
                          <span class="pf-v6-c-nav__link-text">Authentication</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-nav__item">
                        <a href="#" class="pf-v6-c-nav__link" aria-label="Code">
                          <span class="pf-v6-c-nav__link-icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M9.707 9.707 3.414 16l6.293 6.293a.999.999 0 1 1-1.414 1.414l-6.646-6.646a1.501 1.501 0 0 1 0-2.121l6.646-6.646a.999.999 0 1 1 1.414 1.414Zm20.647 5.232-6.646-6.646a.999.999 0 1 0-1.414 1.414L28.587 16l-6.293 6.293a.999.999 0 1 0 1.414 1.414l6.646-6.646a1.501 1.501 0 0 0 0-2.121ZM18.121 6.022a.997.997 0 0 0-1.186.77l-3.826 18a1 1 0 1 0 1.956.416l3.826-18a1 1 0 0 0-.77-1.186Z"
                              />
                            </svg>
                          </span>
                          <span class="pf-v6-c-nav__link-text">Network services</span>
                        </a>
                      </li>
                    </ul>
                  </nav>

                  <div
                    class="pf-v6-c-toolbar__group pf-m-align-end pf-m-spacer-none pf-m-spacer-md-on-md pf-m-action-group-plain"
                  >
                    <div class="pf-v6-c-toolbar__item">
                      <button
                        class="pf-v6-c-menu-toggle pf-m-docked pf-m-text pf-m-plain"
                        type="button"
                        aria-expanded="false"
                        aria-label="Applications"
                      >
                        <span class="pf-v6-c-menu-toggle__icon">
                          <svg
                            class="pf-v6-svg"
                            viewBox="0 0 32 32"
                            fill="currentColor"
                            aria-hidden="true"
                            role="img"
                            width="1em"
                            height="1em"
                          >
                            <path
                              d="M13.75 2H3.25C2.561 2 2 2.561 2 3.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25V3.25C15 2.561 14.439 2 13.75 2ZM13 13H4V4h9v9ZM28.75 2h-10.5C17.561 2 17 2.561 17 3.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25V3.25C30 2.561 29.439 2 28.75 2ZM28 13h-9V4h9v9Zm-14.25 4H3.25C2.561 17 2 17.561 2 18.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25v-10.5c0-.689-.561-1.25-1.25-1.25ZM13 28H4v-9h9v9Zm15.75-11h-10.5c-.689 0-1.25.561-1.25 1.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25v-10.5c0-.689-.561-1.25-1.25-1.25ZM28 28h-9v-9h9v9Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-menu-toggle__text">Applications</span>
                      </button>
                    </div>
                    <div class="pf-v6-c-toolbar__item">
                      <button
                        class="pf-v6-c-button pf-m-docked pf-m-settings pf-m-plain"
                        type="button"
                        aria-label="Settings"
                      >
                        <span class="pf-v6-c-button__icon pf-m-start">
                          <svg
                            class="pf-v6-svg"
                            viewBox="0 0 32 32"
                            fill="currentColor"
                            aria-hidden="true"
                            role="img"
                            width="1em"
                            height="1em"
                          >
                            <path
                              d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-button__text">Settings</span>
                      </button>
                    </div>
                    <div class="pf-v6-c-toolbar__item">
                      <button
                        class="pf-v6-c-menu-toggle pf-m-docked pf-m-text pf-m-plain"
                        type="button"
                        aria-expanded="false"
                        aria-label="Help"
                      >
                        <span class="pf-v6-c-menu-toggle__icon">
                          <svg
                            class="pf-v6-svg"
                            viewBox="0 0 32 32"
                            fill="currentColor"
                            aria-hidden="true"
                            role="img"
                            width="1em"
                            height="1em"
                          >
                            <path
                              d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-menu-toggle__text">Help</span>
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </header>
      </div>
    </div>
    <div class="pf-v6-c-compass__main">
      <div class="pf-v6-c-compass__main-header">
        <div class="pf-v6-c-panel pf-m-glass">
          <div class="pf-v6-c-panel__main">
            <div class="pf-v6-c-panel__main-body">
              <div class="pf-v6-c-compass__main-header-content">
                <div class="pf-v6-c-compass__main-header-title">
                  <h2 class="pf-v6-c-title pf-m-h1">Header</h2>
                </div>
                <div class="pf-v6-c-compass__main-header-toolbar">
                  <div class="pf-v6-c-action-list">
                    <div class="pf-v6-c-action-list__group">
                      <div class="pf-v6-c-action-list__item">
                        <button
                          class="pf-v6-c-button pf-m-primary"
                          type="button"
                        >
                          <span class="pf-v6-c-button__text">action</span>
                        </button>
                      </div>
                      <div class="pf-v6-c-action-list__item">
                        <button
                          class="pf-v6-c-button pf-m-secondary"
                          type="button"
                        >
                          <span class="pf-v6-c-button__text">action</span>
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-compass__content">
        <div
          class="pf-v6-c-panel pf-m-glass pf-m-scrollable-auto-height pf-m-scrollable"
        >
          <div class="pf-v6-c-panel__main">
            <div class="pf-v6-c-panel__main-body">[so much room for activities]</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

```

### Docked nav text expanded

```html isFullscreen isBeta
<div class="pf-v6-c-compass pf-m-animate-smoothly pf-m-docked">
  <div class="pf-v6-c-compass__container">
    <header class="pf-v6-c-masthead pf-m-display-inline">
      <div class="pf-v6-c-masthead__main">
        <span class="pf-v6-c-masthead__toggle">
          <button
            class="pf-v6-c-button pf-m-hamburger pf-m-plain"
            type="button"
            aria-label="Global navigation"
          >
            <span class="pf-v6-c-button__icon">
              <svg
                viewBox="0 0 10 10"
                class="pf-v6-c-button--hamburger-icon pf-v6-svg"
                width="1em"
                height="1em"
              >
                <path
                  class="pf-v6-c-button--hamburger-icon--top"
                  d="M1,1 L9,1"
                />
                <path
                  class="pf-v6-c-button--hamburger-icon--middle"
                  d="M1,5 L9,5"
                />
                <path
                  class="pf-v6-c-button--hamburger-icon--arrow"
                  d="M1,5 L1,5 L1,5"
                />
                <path
                  class="pf-v6-c-button--hamburger-icon--bottom"
                  d="M9,9 L1,9"
                />
              </svg>
            </span>
          </button>
        </span>
        <div class="pf-v6-c-masthead__brand">
          <a class="pf-v6-c-masthead__logo" href="#">
            <svg height="37px" viewBox="0 0 679 158">
              <title>PatternFly</title>
              <defs>
                <linearGradient
                  x1="68%"
                  y1="2.25860997e-13%"
                  x2="32%"
                  y2="100%"
                  id="linearGradient-"
                >
                  <stop stop-color="#2B9AF3" offset="0%" />
                  <stop
                    stop-color="#73BCF7"
                    stop-opacity="0.502212631"
                    offset="100%"
                  />
                </linearGradient>
              </defs>
              <g
                stroke="none"
                stroke-width="1"
                fill="none"
                fill-rule="evenodd"
              >
                <g
                  transform="translate(206.000000, 45.750000)"
                  fill="var(--pf-t--global--text--color--regular)"
                  fill-rule="nonzero"
                >
                  <path
                    d="M0,65.25 L0,2.25 L33.21,2.25 C37.35,2.25 41.025,3.135 44.235,4.905 C47.445,6.675 49.98,9.09 51.84,12.15 C53.7,15.21 54.63,18.72 54.63,22.68 C54.63,26.46 53.7,29.865 51.84,32.895 C49.98,35.925 47.43,38.31 44.19,40.05 C40.95,41.79 37.29,42.66 33.21,42.66 L15.48,42.66 L15.48,65.25 L0,65.25 Z M15.48,29.88 L31.41,29.88 C33.69,29.88 35.52,29.22 36.9,27.9 C38.28,26.58 38.97,24.87 38.97,22.77 C38.97,20.61 38.28,18.855 36.9,17.505 C35.52,16.155 33.69,15.48 31.41,15.48 L15.48,15.48 L15.48,29.88 Z"
                  />
                  <path
                    d="M77.04,66.06 C73.68,66.06 70.695,65.43 68.085,64.17 C65.475,62.91 63.435,61.17 61.965,58.95 C60.495,56.73 59.76,54.18 59.76,51.3 C59.76,46.74 61.485,43.215 64.935,40.725 C68.385,38.235 73.2,36.99 79.38,36.99 C83.1,36.99 86.7,37.44 90.18,38.34 L90.18,36 C90.18,31.26 87.15,28.89 81.09,28.89 C77.49,28.89 72.69,30.15 66.69,32.67 L61.47,21.96 C69.15,18.48 76.56,16.74 83.7,16.74 C90.3,16.74 95.43,18.315 99.09,21.465 C102.75,24.615 104.58,29.04 104.58,34.74 L104.58,65.25 L90.18,65.25 L90.18,62.37 C88.26,63.69 86.235,64.635 84.105,65.205 C81.975,65.775 79.62,66.06 77.04,66.06 Z M73.62,51.03 C73.62,52.53 74.28,53.7 75.6,54.54 C76.92,55.38 78.75,55.8 81.09,55.8 C84.69,55.8 87.72,55.05 90.18,53.55 L90.18,47.43 C87.42,46.71 84.54,46.35 81.54,46.35 C79.02,46.35 77.07,46.755 75.69,47.565 C74.31,48.375 73.62,49.53 73.62,51.03 Z"
                  />
                  <path
                    d="M137.25,65.88 C125.73,65.88 119.97,60.84 119.97,50.76 L119.97,29.79 L110.34,29.79 L110.34,17.64 L119.97,17.64 L119.97,5.4 L134.55,2.25 L134.55,17.64 L147.87,17.64 L147.87,29.79 L134.55,29.79 L134.55,47.88 C134.55,49.98 135.015,51.465 135.945,52.335 C136.875,53.205 138.51,53.64 140.85,53.64 C143.01,53.64 145.2,53.31 147.42,52.65 L147.42,64.44 C146.1,64.86 144.42,65.205 142.38,65.475 C140.34,65.745 138.63,65.88 137.25,65.88 Z"
                  />
                  <path
                    d="M177.57,65.88 C166.05,65.88 160.29,60.84 160.29,50.76 L160.29,29.79 L150.66,29.79 L150.66,17.64 L160.29,17.64 L160.29,5.4 L174.87,2.25 L174.87,17.64 L188.19,17.64 L188.19,29.79 L174.87,29.79 L174.87,47.88 C174.87,49.98 175.335,51.465 176.265,52.335 C177.195,53.205 178.83,53.64 181.17,53.64 C183.33,53.64 185.52,53.31 187.74,52.65 L187.74,64.44 C186.42,64.86 184.74,65.205 182.7,65.475 C180.66,65.745 178.95,65.88 177.57,65.88 Z"
                  />
                  <path
                    d="M217.62,66.15 C212.76,66.15 208.365,65.055 204.435,62.865 C200.505,60.675 197.4,57.72 195.12,54 C192.84,50.28 191.7,46.11 191.7,41.49 C191.7,36.87 192.795,32.7 194.985,28.98 C197.175,25.26 200.16,22.305 203.94,20.115 C207.72,17.925 211.92,16.83 216.54,16.83 C221.22,16.83 225.36,17.955 228.96,20.205 C232.56,22.455 235.395,25.53 237.465,29.43 C239.535,33.33 240.57,37.8 240.57,42.84 L240.57,46.44 L206.64,46.44 C207.6,48.66 209.1,50.475 211.14,51.885 C213.18,53.295 215.58,54 218.34,54 C222.42,54 225.6,52.8 227.88,50.4 L237.51,58.95 C234.51,61.47 231.435,63.3 228.285,64.44 C225.135,65.58 221.58,66.15 217.62,66.15 Z M206.37,36.27 L226.26,36.27 C225.48,33.99 224.205,32.16 222.435,30.78 C220.665,29.4 218.61,28.71 216.27,28.71 C213.87,28.71 211.8,29.37 210.06,30.69 C208.32,32.01 207.09,33.87 206.37,36.27 Z"
                  />
                  <path
                    d="M247.41,65.25 L247.41,17.64 L261.99,17.64 L261.99,22.41 C265.23,18.51 269.4,16.56 274.5,16.56 C277.08,16.62 278.91,17.01 279.99,17.73 L279.99,30.42 C277.95,29.46 275.64,28.98 273.06,28.98 C270.78,28.98 268.665,29.505 266.715,30.555 C264.765,31.605 263.19,33.09 261.99,35.01 L261.99,65.25 L247.41,65.25 Z"
                  />
                  <path
                    d="M286.29,65.25 L286.29,17.64 L300.87,17.64 L300.87,20.88 C304.47,18.12 308.73,16.74 313.65,16.74 C317.37,16.74 320.655,17.55 323.505,19.17 C326.355,20.79 328.59,23.04 330.21,25.92 C331.83,28.8 332.64,32.13 332.64,35.91 L332.64,65.25 L318.06,65.25 L318.06,37.89 C318.06,35.25 317.28,33.15 315.72,31.59 C314.16,30.03 312.06,29.25 309.42,29.25 C305.76,29.25 302.91,30.51 300.87,33.03 L300.87,65.25 L286.29,65.25 Z"
                  />
                  <polygon
                    points="342 65.25 342 2.25 392.04 2.25 392.04 15.66 357.48 15.66 357.48 27.45 380.52 27.45 380.52 40.41 357.48 40.41 357.48 65.25"
                  />
                  <polygon
                    points="399.96 65.25 399.96 2.25 414.54 0 414.54 65.25"
                  />
                  <path
                    d="M429.21,84.69 C428.07,84.69 426.96,84.645 425.88,84.555 C424.8,84.465 423.9,84.33 423.18,84.15 L423.18,71.73 C424.38,71.97 425.88,72.09 427.68,72.09 C432.36,72.09 435.51,70.05 437.13,65.97 L437.13,65.88 L418.86,17.64 L434.97,17.64 L445.5,47.61 L457.74,17.64 L473.49,17.64 L452.16,67.68 C450.42,71.82 448.5,75.135 446.4,77.625 C444.3,80.115 441.87,81.915 439.11,83.025 C436.35,84.135 433.05,84.69 429.21,84.69 Z"
                  />
                </g>
                <g transform="translate(0.000000, 0.000000)">
                  <path
                    d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                    fill="#0066CC"
                  />
                  <path
                    d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                    fill="url(#linearGradient-)"
                  />
                  <path
                    d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                    fill="url(#linearGradient-)"
                    transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                  />
                </g>
              </g>
            </svg>
          </a>
        </div>
      </div>
      <div class="pf-v6-c-masthead__content">
        <div class="pf-v6-c-toolbar pf-m-static">
          <div class="pf-v6-c-toolbar__content">
            <div class="pf-v6-c-toolbar__content-section">
              <div class="pf-v6-c-toolbar__item pf-m-align-end">
                <button
                  class="pf-v6-c-button pf-m-plain"
                  type="button"
                  aria-label="Search"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 512 512"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M505 442.7L405.3 343c-4.5-4.5-10.6-7-17-7H372c27.6-35.3 44-79.7 44-128C416 93.1 322.9 0 208 0S0 93.1 0 208s93.1 208 208 208c48.3 0 92.7-16.4 128-44v16.3c0 6.4 2.5 12.5 7 17l99.7 99.7c9.4 9.4 24.6 9.4 33.9 0l28.3-28.3c9.4-9.4 9.4-24.6.1-34zM208 336c-70.7 0-128-57.2-128-128 0-70.7 57.2-128 128-128 70.7 0 128 57.2 128 128 0 70.7-57.2 128-128 128z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
    <div class="pf-v6-c-compass__dock pf-m-text-expanded">
      <div class="pf-v6-c-compass__dock-main">
        <div class="pf-v6-c-skip-to-content">
          <a class="pf-v6-c-button pf-m-primary" href="#main-content-">
            <span class="pf-v6-c-button__text">Skip to content</span>
          </a>
        </div>

        <header
          class="pf-v6-c-masthead pf-m-docked"
          id="compass-docked-text-expanded-example-masthead"
        >
          <div class="pf-v6-c-masthead__main">
            <span class="pf-v6-c-masthead__toggle">
              <button
                class="pf-v6-c-button pf-m-hamburger pf-m-plain"
                type="button"
                aria-label="Global navigation"
              >
                <span class="pf-v6-c-button__icon">
                  <svg
                    viewBox="0 0 10 10"
                    class="pf-v6-c-button--hamburger-icon pf-v6-svg"
                    width="1em"
                    height="1em"
                  >
                    <path
                      class="pf-v6-c-button--hamburger-icon--top"
                      d="M1,1 L9,1"
                    />
                    <path
                      class="pf-v6-c-button--hamburger-icon--middle"
                      d="M1,5 L9,5"
                    />
                    <path
                      class="pf-v6-c-button--hamburger-icon--arrow"
                      d="M1,5 L1,5 L1,5"
                    />
                    <path
                      class="pf-v6-c-button--hamburger-icon--bottom"
                      d="M9,9 L1,9"
                    />
                  </svg>
                </span>
              </button>
            </span>
            <div class="pf-v6-c-masthead__brand">
              <a class="pf-v6-c-masthead__logo" href="#">
                <svg height="37px" viewBox="0 0 679 158">
                  <title>PatternFly</title>
                  <defs>
                    <linearGradient
                      x1="68%"
                      y1="2.25860997e-13%"
                      x2="32%"
                      y2="100%"
                      id="linearGradient-compass-docked-text-expanded-example-masthead"
                    >
                      <stop stop-color="#2B9AF3" offset="0%" />
                      <stop
                        stop-color="#73BCF7"
                        stop-opacity="0.502212631"
                        offset="100%"
                      />
                    </linearGradient>
                  </defs>
                  <g
                    stroke="none"
                    stroke-width="1"
                    fill="none"
                    fill-rule="evenodd"
                  >
                    <g
                      transform="translate(206.000000, 45.750000)"
                      fill="var(--pf-t--global--text--color--regular)"
                      fill-rule="nonzero"
                    >
                      <path
                        d="M0,65.25 L0,2.25 L33.21,2.25 C37.35,2.25 41.025,3.135 44.235,4.905 C47.445,6.675 49.98,9.09 51.84,12.15 C53.7,15.21 54.63,18.72 54.63,22.68 C54.63,26.46 53.7,29.865 51.84,32.895 C49.98,35.925 47.43,38.31 44.19,40.05 C40.95,41.79 37.29,42.66 33.21,42.66 L15.48,42.66 L15.48,65.25 L0,65.25 Z M15.48,29.88 L31.41,29.88 C33.69,29.88 35.52,29.22 36.9,27.9 C38.28,26.58 38.97,24.87 38.97,22.77 C38.97,20.61 38.28,18.855 36.9,17.505 C35.52,16.155 33.69,15.48 31.41,15.48 L15.48,15.48 L15.48,29.88 Z"
                      />
                      <path
                        d="M77.04,66.06 C73.68,66.06 70.695,65.43 68.085,64.17 C65.475,62.91 63.435,61.17 61.965,58.95 C60.495,56.73 59.76,54.18 59.76,51.3 C59.76,46.74 61.485,43.215 64.935,40.725 C68.385,38.235 73.2,36.99 79.38,36.99 C83.1,36.99 86.7,37.44 90.18,38.34 L90.18,36 C90.18,31.26 87.15,28.89 81.09,28.89 C77.49,28.89 72.69,30.15 66.69,32.67 L61.47,21.96 C69.15,18.48 76.56,16.74 83.7,16.74 C90.3,16.74 95.43,18.315 99.09,21.465 C102.75,24.615 104.58,29.04 104.58,34.74 L104.58,65.25 L90.18,65.25 L90.18,62.37 C88.26,63.69 86.235,64.635 84.105,65.205 C81.975,65.775 79.62,66.06 77.04,66.06 Z M73.62,51.03 C73.62,52.53 74.28,53.7 75.6,54.54 C76.92,55.38 78.75,55.8 81.09,55.8 C84.69,55.8 87.72,55.05 90.18,53.55 L90.18,47.43 C87.42,46.71 84.54,46.35 81.54,46.35 C79.02,46.35 77.07,46.755 75.69,47.565 C74.31,48.375 73.62,49.53 73.62,51.03 Z"
                      />
                      <path
                        d="M137.25,65.88 C125.73,65.88 119.97,60.84 119.97,50.76 L119.97,29.79 L110.34,29.79 L110.34,17.64 L119.97,17.64 L119.97,5.4 L134.55,2.25 L134.55,17.64 L147.87,17.64 L147.87,29.79 L134.55,29.79 L134.55,47.88 C134.55,49.98 135.015,51.465 135.945,52.335 C136.875,53.205 138.51,53.64 140.85,53.64 C143.01,53.64 145.2,53.31 147.42,52.65 L147.42,64.44 C146.1,64.86 144.42,65.205 142.38,65.475 C140.34,65.745 138.63,65.88 137.25,65.88 Z"
                      />
                      <path
                        d="M177.57,65.88 C166.05,65.88 160.29,60.84 160.29,50.76 L160.29,29.79 L150.66,29.79 L150.66,17.64 L160.29,17.64 L160.29,5.4 L174.87,2.25 L174.87,17.64 L188.19,17.64 L188.19,29.79 L174.87,29.79 L174.87,47.88 C174.87,49.98 175.335,51.465 176.265,52.335 C177.195,53.205 178.83,53.64 181.17,53.64 C183.33,53.64 185.52,53.31 187.74,52.65 L187.74,64.44 C186.42,64.86 184.74,65.205 182.7,65.475 C180.66,65.745 178.95,65.88 177.57,65.88 Z"
                      />
                      <path
                        d="M217.62,66.15 C212.76,66.15 208.365,65.055 204.435,62.865 C200.505,60.675 197.4,57.72 195.12,54 C192.84,50.28 191.7,46.11 191.7,41.49 C191.7,36.87 192.795,32.7 194.985,28.98 C197.175,25.26 200.16,22.305 203.94,20.115 C207.72,17.925 211.92,16.83 216.54,16.83 C221.22,16.83 225.36,17.955 228.96,20.205 C232.56,22.455 235.395,25.53 237.465,29.43 C239.535,33.33 240.57,37.8 240.57,42.84 L240.57,46.44 L206.64,46.44 C207.6,48.66 209.1,50.475 211.14,51.885 C213.18,53.295 215.58,54 218.34,54 C222.42,54 225.6,52.8 227.88,50.4 L237.51,58.95 C234.51,61.47 231.435,63.3 228.285,64.44 C225.135,65.58 221.58,66.15 217.62,66.15 Z M206.37,36.27 L226.26,36.27 C225.48,33.99 224.205,32.16 222.435,30.78 C220.665,29.4 218.61,28.71 216.27,28.71 C213.87,28.71 211.8,29.37 210.06,30.69 C208.32,32.01 207.09,33.87 206.37,36.27 Z"
                      />
                      <path
                        d="M247.41,65.25 L247.41,17.64 L261.99,17.64 L261.99,22.41 C265.23,18.51 269.4,16.56 274.5,16.56 C277.08,16.62 278.91,17.01 279.99,17.73 L279.99,30.42 C277.95,29.46 275.64,28.98 273.06,28.98 C270.78,28.98 268.665,29.505 266.715,30.555 C264.765,31.605 263.19,33.09 261.99,35.01 L261.99,65.25 L247.41,65.25 Z"
                      />
                      <path
                        d="M286.29,65.25 L286.29,17.64 L300.87,17.64 L300.87,20.88 C304.47,18.12 308.73,16.74 313.65,16.74 C317.37,16.74 320.655,17.55 323.505,19.17 C326.355,20.79 328.59,23.04 330.21,25.92 C331.83,28.8 332.64,32.13 332.64,35.91 L332.64,65.25 L318.06,65.25 L318.06,37.89 C318.06,35.25 317.28,33.15 315.72,31.59 C314.16,30.03 312.06,29.25 309.42,29.25 C305.76,29.25 302.91,30.51 300.87,33.03 L300.87,65.25 L286.29,65.25 Z"
                      />
                      <polygon
                        points="342 65.25 342 2.25 392.04 2.25 392.04 15.66 357.48 15.66 357.48 27.45 380.52 27.45 380.52 40.41 357.48 40.41 357.48 65.25"
                      />
                      <polygon
                        points="399.96 65.25 399.96 2.25 414.54 0 414.54 65.25"
                      />
                      <path
                        d="M429.21,84.69 C428.07,84.69 426.96,84.645 425.88,84.555 C424.8,84.465 423.9,84.33 423.18,84.15 L423.18,71.73 C424.38,71.97 425.88,72.09 427.68,72.09 C432.36,72.09 435.51,70.05 437.13,65.97 L437.13,65.88 L418.86,17.64 L434.97,17.64 L445.5,47.61 L457.74,17.64 L473.49,17.64 L452.16,67.68 C450.42,71.82 448.5,75.135 446.4,77.625 C444.3,80.115 441.87,81.915 439.11,83.025 C436.35,84.135 433.05,84.69 429.21,84.69 Z"
                      />
                    </g>
                    <g transform="translate(0.000000, 0.000000)">
                      <path
                        d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                        fill="#0066CC"
                      />
                      <path
                        d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                        fill="url(#linearGradient-compass-docked-text-expanded-example-masthead)"
                      />
                      <path
                        d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                        fill="url(#linearGradient-compass-docked-text-expanded-example-masthead)"
                        transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                      />
                    </g>
                  </g>
                </svg>
              </a>
              <a class="pf-v6-c-masthead__logo pf-m-compact" href="#">
                <svg width="37px" height="37px" viewBox="0 0 158 158">
                  <title>PatternFly</title>
                  <defs>
                    <linearGradient
                      x1="68%"
                      y1="2.25860997e-13%"
                      x2="32%"
                      y2="100%"
                      id="linearGradient-1"
                    >
                      <stop stop-color="#2B9AF3" offset="0%" />
                      <stop
                        stop-color="#73BCF7"
                        stop-opacity="0.502212631"
                        offset="100%"
                      />
                    </linearGradient>
                  </defs>
                  <g
                    id="PF-IconLogo-color"
                    stroke="none"
                    stroke-width="1"
                    fill="none"
                    fill-rule="evenodd"
                  >
                    <g id="Logo">
                      <path
                        d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                        id="Rectangle-Copy-17"
                        fill="#0066CC"
                      />
                      <path
                        d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                        id="Path-2"
                        fill="url(#linearGradient-1)"
                      />
                      <path
                        d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                        id="Path-2"
                        fill="url(#linearGradient-1)"
                        transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                      />
                    </g>
                  </g>
                </svg>
              </a>
            </div>
          </div>
          <hr class="pf-v6-c-divider" />
          <div class="pf-v6-c-masthead__content">
            <div
              class="pf-v6-c-toolbar pf-m-vertical pf-m-static"
              id="compass-docked-text-expanded-example-masthead-toolbar"
            >
              <div class="pf-v6-c-toolbar__content">
                <div class="pf-v6-c-toolbar__content-section">
                  <nav class="pf-v6-c-nav pf-m-docked" aria-label="Global">
                    <ul class="pf-v6-c-nav__list" role="list">
                      <li class="pf-v6-c-nav__item">
                        <a
                          href="#"
                          class="pf-v6-c-nav__link"
                          aria-label="Cubes"
                        >
                          <span class="pf-v6-c-nav__link-icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M12.5 12h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5v7c0 .827.673 1.5 1.5 1.5Zm.5-8h6v6h-6V4ZM5.5 25h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5v7c0 .827.673 1.5 1.5 1.5Zm.5-8h6v6H6v-6Zm24 12a1 1 0 0 1-1 1H3a1 1 0 0 1 0-2h26a1 1 0 0 1 1 1ZM18 16.5v7c0 .827.673 1.5 1.5 1.5h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5Zm2 .5h6v6h-6v-6Z"
                              />
                            </svg>
                          </span>
                          <span class="pf-v6-c-nav__link-text">System panel</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-nav__item">
                        <a
                          href="#"
                          class="pf-v6-c-nav__link pf-m-current"
                          aria-current="page"
                          aria-label="Folder"
                        >
                          <span class="pf-v6-c-nav__link-icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M29.5 8H17.81l-.681-3.208A1 1 0 0 0 16.15 4h-9.3a1 1 0 0 0-.979.792L5.19 8H2.5C1.673 8 1 8.673 1 9.5v17c0 .827.673 1.5 1.5 1.5h27c.827 0 1.5-.673 1.5-1.5v-17c0-.827-.673-1.5-1.5-1.5ZM29 26H3V10h3a1 1 0 0 0 .979-.792L7.66 6h7.682l.681 3.208a1 1 0 0 0 .979.792h12v16Z"
                              />
                            </svg>
                          </span>
                          <span class="pf-v6-c-nav__link-text">Policy</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-nav__item">
                        <a
                          href="#"
                          class="pf-v6-c-nav__link"
                          aria-label="Cloud"
                        >
                          <span class="pf-v6-c-nav__link-icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M26.996 14.228c.003-.077.004-.153.004-.228 0-4.962-4.037-9-9-9-3.899 0-7.333 2.532-8.54 6.156A6.891 6.891 0 0 0 8 11c-3.859 0-7 3.14-7 7s3.141 7 7 7h17.5c3.032 0 5.5-2.467 5.5-5.5a5.456 5.456 0 0 0-4.004-5.272ZM25.5 23H8c-2.757 0-5-2.243-5-5s2.243-5 5-5a4.97 4.97 0 0 1 1.799.34 1.003 1.003 0 0 0 1.341-.735C11.796 9.357 14.682 7 18 7c3.859 0 7 3.14 7 7 0 .311-.028.615-.067.916a1.004 1.004 0 0 0 .898 1.123 3.473 3.473 0 0 1 3.17 3.461c0 1.93-1.57 3.5-3.5 3.5Z"
                              />
                            </svg>
                          </span>
                          <span class="pf-v6-c-nav__link-text">Authentication</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-nav__item">
                        <a href="#" class="pf-v6-c-nav__link" aria-label="Code">
                          <span class="pf-v6-c-nav__link-icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M9.707 9.707 3.414 16l6.293 6.293a.999.999 0 1 1-1.414 1.414l-6.646-6.646a1.501 1.501 0 0 1 0-2.121l6.646-6.646a.999.999 0 1 1 1.414 1.414Zm20.647 5.232-6.646-6.646a.999.999 0 1 0-1.414 1.414L28.587 16l-6.293 6.293a.999.999 0 1 0 1.414 1.414l6.646-6.646a1.501 1.501 0 0 0 0-2.121ZM18.121 6.022a.997.997 0 0 0-1.186.77l-3.826 18a1 1 0 1 0 1.956.416l3.826-18a1 1 0 0 0-.77-1.186Z"
                              />
                            </svg>
                          </span>
                          <span class="pf-v6-c-nav__link-text">Network services</span>
                        </a>
                      </li>
                    </ul>
                  </nav>

                  <div
                    class="pf-v6-c-toolbar__group pf-m-align-end pf-m-spacer-none pf-m-spacer-md-on-md pf-m-action-group-plain"
                  >
                    <div class="pf-v6-c-toolbar__item">
                      <button
                        class="pf-v6-c-menu-toggle pf-m-docked pf-m-text pf-m-plain"
                        type="button"
                        aria-expanded="false"
                        aria-label="Applications"
                      >
                        <span class="pf-v6-c-menu-toggle__icon">
                          <svg
                            class="pf-v6-svg"
                            viewBox="0 0 32 32"
                            fill="currentColor"
                            aria-hidden="true"
                            role="img"
                            width="1em"
                            height="1em"
                          >
                            <path
                              d="M13.75 2H3.25C2.561 2 2 2.561 2 3.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25V3.25C15 2.561 14.439 2 13.75 2ZM13 13H4V4h9v9ZM28.75 2h-10.5C17.561 2 17 2.561 17 3.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25V3.25C30 2.561 29.439 2 28.75 2ZM28 13h-9V4h9v9Zm-14.25 4H3.25C2.561 17 2 17.561 2 18.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25v-10.5c0-.689-.561-1.25-1.25-1.25ZM13 28H4v-9h9v9Zm15.75-11h-10.5c-.689 0-1.25.561-1.25 1.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25v-10.5c0-.689-.561-1.25-1.25-1.25ZM28 28h-9v-9h9v9Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-menu-toggle__text">Applications</span>
                      </button>
                    </div>
                    <div class="pf-v6-c-toolbar__item">
                      <button
                        class="pf-v6-c-button pf-m-docked pf-m-settings pf-m-plain"
                        type="button"
                        aria-label="Settings"
                      >
                        <span class="pf-v6-c-button__icon pf-m-start">
                          <svg
                            class="pf-v6-svg"
                            viewBox="0 0 32 32"
                            fill="currentColor"
                            aria-hidden="true"
                            role="img"
                            width="1em"
                            height="1em"
                          >
                            <path
                              d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-button__text">Settings</span>
                      </button>
                    </div>
                    <div class="pf-v6-c-toolbar__item">
                      <button
                        class="pf-v6-c-menu-toggle pf-m-docked pf-m-text pf-m-plain"
                        type="button"
                        aria-expanded="false"
                        aria-label="Help"
                      >
                        <span class="pf-v6-c-menu-toggle__icon">
                          <svg
                            class="pf-v6-svg"
                            viewBox="0 0 32 32"
                            fill="currentColor"
                            aria-hidden="true"
                            role="img"
                            width="1em"
                            height="1em"
                          >
                            <path
                              d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-menu-toggle__text">Help</span>
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </header>
      </div>
    </div>
    <div class="pf-v6-c-compass__main">
      <div class="pf-v6-c-compass__main-header">
        <div class="pf-v6-c-panel pf-m-glass">
          <div class="pf-v6-c-panel__main">
            <div class="pf-v6-c-panel__main-body">
              <div class="pf-v6-c-compass__main-header-content">
                <div class="pf-v6-c-compass__main-header-title">
                  <h2 class="pf-v6-c-title pf-m-h1">Header</h2>
                </div>
                <div class="pf-v6-c-compass__main-header-toolbar">
                  <div class="pf-v6-c-action-list">
                    <div class="pf-v6-c-action-list__group">
                      <div class="pf-v6-c-action-list__item">
                        <button
                          class="pf-v6-c-button pf-m-primary"
                          type="button"
                        >
                          <span class="pf-v6-c-button__text">action</span>
                        </button>
                      </div>
                      <div class="pf-v6-c-action-list__item">
                        <button
                          class="pf-v6-c-button pf-m-secondary"
                          type="button"
                        >
                          <span class="pf-v6-c-button__text">action</span>
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-compass__content">
        <div
          class="pf-v6-c-panel pf-m-glass pf-m-scrollable-auto-height pf-m-scrollable"
        >
          <div class="pf-v6-c-panel__main">
            <div class="pf-v6-c-panel__main-body">[so much room for activities]</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

```

### Docked nav text expanded - expanded on mobile

```html isFullscreen isBeta
<div class="pf-v6-c-compass pf-m-animate-smoothly pf-m-docked">
  <div class="pf-v6-c-compass__container">
    <header class="pf-v6-c-masthead pf-m-display-inline">
      <div class="pf-v6-c-masthead__main">
        <span class="pf-v6-c-masthead__toggle">
          <button
            class="pf-v6-c-button pf-m-hamburger pf-m-plain"
            type="button"
            aria-label="Global navigation"
          >
            <span class="pf-v6-c-button__icon">
              <svg
                viewBox="0 0 10 10"
                class="pf-v6-c-button--hamburger-icon pf-v6-svg"
                width="1em"
                height="1em"
              >
                <path
                  class="pf-v6-c-button--hamburger-icon--top"
                  d="M1,1 L9,1"
                />
                <path
                  class="pf-v6-c-button--hamburger-icon--middle"
                  d="M1,5 L9,5"
                />
                <path
                  class="pf-v6-c-button--hamburger-icon--arrow"
                  d="M1,5 L1,5 L1,5"
                />
                <path
                  class="pf-v6-c-button--hamburger-icon--bottom"
                  d="M9,9 L1,9"
                />
              </svg>
            </span>
          </button>
        </span>
        <div class="pf-v6-c-masthead__brand">
          <a class="pf-v6-c-masthead__logo" href="#">
            <svg height="37px" viewBox="0 0 679 158">
              <title>PatternFly</title>
              <defs>
                <linearGradient
                  x1="68%"
                  y1="2.25860997e-13%"
                  x2="32%"
                  y2="100%"
                  id="linearGradient-"
                >
                  <stop stop-color="#2B9AF3" offset="0%" />
                  <stop
                    stop-color="#73BCF7"
                    stop-opacity="0.502212631"
                    offset="100%"
                  />
                </linearGradient>
              </defs>
              <g
                stroke="none"
                stroke-width="1"
                fill="none"
                fill-rule="evenodd"
              >
                <g
                  transform="translate(206.000000, 45.750000)"
                  fill="var(--pf-t--global--text--color--regular)"
                  fill-rule="nonzero"
                >
                  <path
                    d="M0,65.25 L0,2.25 L33.21,2.25 C37.35,2.25 41.025,3.135 44.235,4.905 C47.445,6.675 49.98,9.09 51.84,12.15 C53.7,15.21 54.63,18.72 54.63,22.68 C54.63,26.46 53.7,29.865 51.84,32.895 C49.98,35.925 47.43,38.31 44.19,40.05 C40.95,41.79 37.29,42.66 33.21,42.66 L15.48,42.66 L15.48,65.25 L0,65.25 Z M15.48,29.88 L31.41,29.88 C33.69,29.88 35.52,29.22 36.9,27.9 C38.28,26.58 38.97,24.87 38.97,22.77 C38.97,20.61 38.28,18.855 36.9,17.505 C35.52,16.155 33.69,15.48 31.41,15.48 L15.48,15.48 L15.48,29.88 Z"
                  />
                  <path
                    d="M77.04,66.06 C73.68,66.06 70.695,65.43 68.085,64.17 C65.475,62.91 63.435,61.17 61.965,58.95 C60.495,56.73 59.76,54.18 59.76,51.3 C59.76,46.74 61.485,43.215 64.935,40.725 C68.385,38.235 73.2,36.99 79.38,36.99 C83.1,36.99 86.7,37.44 90.18,38.34 L90.18,36 C90.18,31.26 87.15,28.89 81.09,28.89 C77.49,28.89 72.69,30.15 66.69,32.67 L61.47,21.96 C69.15,18.48 76.56,16.74 83.7,16.74 C90.3,16.74 95.43,18.315 99.09,21.465 C102.75,24.615 104.58,29.04 104.58,34.74 L104.58,65.25 L90.18,65.25 L90.18,62.37 C88.26,63.69 86.235,64.635 84.105,65.205 C81.975,65.775 79.62,66.06 77.04,66.06 Z M73.62,51.03 C73.62,52.53 74.28,53.7 75.6,54.54 C76.92,55.38 78.75,55.8 81.09,55.8 C84.69,55.8 87.72,55.05 90.18,53.55 L90.18,47.43 C87.42,46.71 84.54,46.35 81.54,46.35 C79.02,46.35 77.07,46.755 75.69,47.565 C74.31,48.375 73.62,49.53 73.62,51.03 Z"
                  />
                  <path
                    d="M137.25,65.88 C125.73,65.88 119.97,60.84 119.97,50.76 L119.97,29.79 L110.34,29.79 L110.34,17.64 L119.97,17.64 L119.97,5.4 L134.55,2.25 L134.55,17.64 L147.87,17.64 L147.87,29.79 L134.55,29.79 L134.55,47.88 C134.55,49.98 135.015,51.465 135.945,52.335 C136.875,53.205 138.51,53.64 140.85,53.64 C143.01,53.64 145.2,53.31 147.42,52.65 L147.42,64.44 C146.1,64.86 144.42,65.205 142.38,65.475 C140.34,65.745 138.63,65.88 137.25,65.88 Z"
                  />
                  <path
                    d="M177.57,65.88 C166.05,65.88 160.29,60.84 160.29,50.76 L160.29,29.79 L150.66,29.79 L150.66,17.64 L160.29,17.64 L160.29,5.4 L174.87,2.25 L174.87,17.64 L188.19,17.64 L188.19,29.79 L174.87,29.79 L174.87,47.88 C174.87,49.98 175.335,51.465 176.265,52.335 C177.195,53.205 178.83,53.64 181.17,53.64 C183.33,53.64 185.52,53.31 187.74,52.65 L187.74,64.44 C186.42,64.86 184.74,65.205 182.7,65.475 C180.66,65.745 178.95,65.88 177.57,65.88 Z"
                  />
                  <path
                    d="M217.62,66.15 C212.76,66.15 208.365,65.055 204.435,62.865 C200.505,60.675 197.4,57.72 195.12,54 C192.84,50.28 191.7,46.11 191.7,41.49 C191.7,36.87 192.795,32.7 194.985,28.98 C197.175,25.26 200.16,22.305 203.94,20.115 C207.72,17.925 211.92,16.83 216.54,16.83 C221.22,16.83 225.36,17.955 228.96,20.205 C232.56,22.455 235.395,25.53 237.465,29.43 C239.535,33.33 240.57,37.8 240.57,42.84 L240.57,46.44 L206.64,46.44 C207.6,48.66 209.1,50.475 211.14,51.885 C213.18,53.295 215.58,54 218.34,54 C222.42,54 225.6,52.8 227.88,50.4 L237.51,58.95 C234.51,61.47 231.435,63.3 228.285,64.44 C225.135,65.58 221.58,66.15 217.62,66.15 Z M206.37,36.27 L226.26,36.27 C225.48,33.99 224.205,32.16 222.435,30.78 C220.665,29.4 218.61,28.71 216.27,28.71 C213.87,28.71 211.8,29.37 210.06,30.69 C208.32,32.01 207.09,33.87 206.37,36.27 Z"
                  />
                  <path
                    d="M247.41,65.25 L247.41,17.64 L261.99,17.64 L261.99,22.41 C265.23,18.51 269.4,16.56 274.5,16.56 C277.08,16.62 278.91,17.01 279.99,17.73 L279.99,30.42 C277.95,29.46 275.64,28.98 273.06,28.98 C270.78,28.98 268.665,29.505 266.715,30.555 C264.765,31.605 263.19,33.09 261.99,35.01 L261.99,65.25 L247.41,65.25 Z"
                  />
                  <path
                    d="M286.29,65.25 L286.29,17.64 L300.87,17.64 L300.87,20.88 C304.47,18.12 308.73,16.74 313.65,16.74 C317.37,16.74 320.655,17.55 323.505,19.17 C326.355,20.79 328.59,23.04 330.21,25.92 C331.83,28.8 332.64,32.13 332.64,35.91 L332.64,65.25 L318.06,65.25 L318.06,37.89 C318.06,35.25 317.28,33.15 315.72,31.59 C314.16,30.03 312.06,29.25 309.42,29.25 C305.76,29.25 302.91,30.51 300.87,33.03 L300.87,65.25 L286.29,65.25 Z"
                  />
                  <polygon
                    points="342 65.25 342 2.25 392.04 2.25 392.04 15.66 357.48 15.66 357.48 27.45 380.52 27.45 380.52 40.41 357.48 40.41 357.48 65.25"
                  />
                  <polygon
                    points="399.96 65.25 399.96 2.25 414.54 0 414.54 65.25"
                  />
                  <path
                    d="M429.21,84.69 C428.07,84.69 426.96,84.645 425.88,84.555 C424.8,84.465 423.9,84.33 423.18,84.15 L423.18,71.73 C424.38,71.97 425.88,72.09 427.68,72.09 C432.36,72.09 435.51,70.05 437.13,65.97 L437.13,65.88 L418.86,17.64 L434.97,17.64 L445.5,47.61 L457.74,17.64 L473.49,17.64 L452.16,67.68 C450.42,71.82 448.5,75.135 446.4,77.625 C444.3,80.115 441.87,81.915 439.11,83.025 C436.35,84.135 433.05,84.69 429.21,84.69 Z"
                  />
                </g>
                <g transform="translate(0.000000, 0.000000)">
                  <path
                    d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                    fill="#0066CC"
                  />
                  <path
                    d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                    fill="url(#linearGradient-)"
                  />
                  <path
                    d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                    fill="url(#linearGradient-)"
                    transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                  />
                </g>
              </g>
            </svg>
          </a>
        </div>
      </div>
      <div class="pf-v6-c-masthead__content">
        <div class="pf-v6-c-toolbar pf-m-static">
          <div class="pf-v6-c-toolbar__content">
            <div class="pf-v6-c-toolbar__content-section">
              <div class="pf-v6-c-toolbar__item pf-m-align-end">
                <button
                  class="pf-v6-c-button pf-m-plain"
                  type="button"
                  aria-label="Search"
                >
                  <span class="pf-v6-c-button__icon">
                    <svg
                      class="pf-v6-svg"
                      viewBox="0 0 512 512"
                      fill="currentColor"
                      aria-hidden="true"
                      role="img"
                      width="1em"
                      height="1em"
                    >
                      <path
                        d="M505 442.7L405.3 343c-4.5-4.5-10.6-7-17-7H372c27.6-35.3 44-79.7 44-128C416 93.1 322.9 0 208 0S0 93.1 0 208s93.1 208 208 208c48.3 0 92.7-16.4 128-44v16.3c0 6.4 2.5 12.5 7 17l99.7 99.7c9.4 9.4 24.6 9.4 33.9 0l28.3-28.3c9.4-9.4 9.4-24.6.1-34zM208 336c-70.7 0-128-57.2-128-128 0-70.7 57.2-128 128-128 70.7 0 128 57.2 128 128 0 70.7-57.2 128-128 128z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
    <div class="pf-v6-c-compass__dock pf-m-text-expanded pf-m-expanded">
      <div class="pf-v6-c-compass__dock-main">
        <div class="pf-v6-c-skip-to-content">
          <a class="pf-v6-c-button pf-m-primary" href="#main-content-">
            <span class="pf-v6-c-button__text">Skip to content</span>
          </a>
        </div>

        <header
          class="pf-v6-c-masthead pf-m-docked"
          id="compass-docked-text-expanded-mobile-expanded-example-masthead"
        >
          <div class="pf-v6-c-masthead__main">
            <span class="pf-v6-c-masthead__toggle">
              <button
                class="pf-v6-c-button pf-m-hamburger pf-m-plain"
                type="button"
                aria-label="Global navigation"
              >
                <span class="pf-v6-c-button__icon">
                  <svg
                    viewBox="0 0 10 10"
                    class="pf-v6-c-button--hamburger-icon pf-v6-svg"
                    width="1em"
                    height="1em"
                  >
                    <path
                      class="pf-v6-c-button--hamburger-icon--top"
                      d="M1,1 L9,1"
                    />
                    <path
                      class="pf-v6-c-button--hamburger-icon--middle"
                      d="M1,5 L9,5"
                    />
                    <path
                      class="pf-v6-c-button--hamburger-icon--arrow"
                      d="M1,5 L1,5 L1,5"
                    />
                    <path
                      class="pf-v6-c-button--hamburger-icon--bottom"
                      d="M9,9 L1,9"
                    />
                  </svg>
                </span>
              </button>
            </span>
            <div class="pf-v6-c-masthead__brand">
              <a class="pf-v6-c-masthead__logo" href="#">
                <svg height="37px" viewBox="0 0 679 158">
                  <title>PatternFly</title>
                  <defs>
                    <linearGradient
                      x1="68%"
                      y1="2.25860997e-13%"
                      x2="32%"
                      y2="100%"
                      id="linearGradient-compass-docked-text-expanded-mobile-expanded-example-masthead"
                    >
                      <stop stop-color="#2B9AF3" offset="0%" />
                      <stop
                        stop-color="#73BCF7"
                        stop-opacity="0.502212631"
                        offset="100%"
                      />
                    </linearGradient>
                  </defs>
                  <g
                    stroke="none"
                    stroke-width="1"
                    fill="none"
                    fill-rule="evenodd"
                  >
                    <g
                      transform="translate(206.000000, 45.750000)"
                      fill="var(--pf-t--global--text--color--regular)"
                      fill-rule="nonzero"
                    >
                      <path
                        d="M0,65.25 L0,2.25 L33.21,2.25 C37.35,2.25 41.025,3.135 44.235,4.905 C47.445,6.675 49.98,9.09 51.84,12.15 C53.7,15.21 54.63,18.72 54.63,22.68 C54.63,26.46 53.7,29.865 51.84,32.895 C49.98,35.925 47.43,38.31 44.19,40.05 C40.95,41.79 37.29,42.66 33.21,42.66 L15.48,42.66 L15.48,65.25 L0,65.25 Z M15.48,29.88 L31.41,29.88 C33.69,29.88 35.52,29.22 36.9,27.9 C38.28,26.58 38.97,24.87 38.97,22.77 C38.97,20.61 38.28,18.855 36.9,17.505 C35.52,16.155 33.69,15.48 31.41,15.48 L15.48,15.48 L15.48,29.88 Z"
                      />
                      <path
                        d="M77.04,66.06 C73.68,66.06 70.695,65.43 68.085,64.17 C65.475,62.91 63.435,61.17 61.965,58.95 C60.495,56.73 59.76,54.18 59.76,51.3 C59.76,46.74 61.485,43.215 64.935,40.725 C68.385,38.235 73.2,36.99 79.38,36.99 C83.1,36.99 86.7,37.44 90.18,38.34 L90.18,36 C90.18,31.26 87.15,28.89 81.09,28.89 C77.49,28.89 72.69,30.15 66.69,32.67 L61.47,21.96 C69.15,18.48 76.56,16.74 83.7,16.74 C90.3,16.74 95.43,18.315 99.09,21.465 C102.75,24.615 104.58,29.04 104.58,34.74 L104.58,65.25 L90.18,65.25 L90.18,62.37 C88.26,63.69 86.235,64.635 84.105,65.205 C81.975,65.775 79.62,66.06 77.04,66.06 Z M73.62,51.03 C73.62,52.53 74.28,53.7 75.6,54.54 C76.92,55.38 78.75,55.8 81.09,55.8 C84.69,55.8 87.72,55.05 90.18,53.55 L90.18,47.43 C87.42,46.71 84.54,46.35 81.54,46.35 C79.02,46.35 77.07,46.755 75.69,47.565 C74.31,48.375 73.62,49.53 73.62,51.03 Z"
                      />
                      <path
                        d="M137.25,65.88 C125.73,65.88 119.97,60.84 119.97,50.76 L119.97,29.79 L110.34,29.79 L110.34,17.64 L119.97,17.64 L119.97,5.4 L134.55,2.25 L134.55,17.64 L147.87,17.64 L147.87,29.79 L134.55,29.79 L134.55,47.88 C134.55,49.98 135.015,51.465 135.945,52.335 C136.875,53.205 138.51,53.64 140.85,53.64 C143.01,53.64 145.2,53.31 147.42,52.65 L147.42,64.44 C146.1,64.86 144.42,65.205 142.38,65.475 C140.34,65.745 138.63,65.88 137.25,65.88 Z"
                      />
                      <path
                        d="M177.57,65.88 C166.05,65.88 160.29,60.84 160.29,50.76 L160.29,29.79 L150.66,29.79 L150.66,17.64 L160.29,17.64 L160.29,5.4 L174.87,2.25 L174.87,17.64 L188.19,17.64 L188.19,29.79 L174.87,29.79 L174.87,47.88 C174.87,49.98 175.335,51.465 176.265,52.335 C177.195,53.205 178.83,53.64 181.17,53.64 C183.33,53.64 185.52,53.31 187.74,52.65 L187.74,64.44 C186.42,64.86 184.74,65.205 182.7,65.475 C180.66,65.745 178.95,65.88 177.57,65.88 Z"
                      />
                      <path
                        d="M217.62,66.15 C212.76,66.15 208.365,65.055 204.435,62.865 C200.505,60.675 197.4,57.72 195.12,54 C192.84,50.28 191.7,46.11 191.7,41.49 C191.7,36.87 192.795,32.7 194.985,28.98 C197.175,25.26 200.16,22.305 203.94,20.115 C207.72,17.925 211.92,16.83 216.54,16.83 C221.22,16.83 225.36,17.955 228.96,20.205 C232.56,22.455 235.395,25.53 237.465,29.43 C239.535,33.33 240.57,37.8 240.57,42.84 L240.57,46.44 L206.64,46.44 C207.6,48.66 209.1,50.475 211.14,51.885 C213.18,53.295 215.58,54 218.34,54 C222.42,54 225.6,52.8 227.88,50.4 L237.51,58.95 C234.51,61.47 231.435,63.3 228.285,64.44 C225.135,65.58 221.58,66.15 217.62,66.15 Z M206.37,36.27 L226.26,36.27 C225.48,33.99 224.205,32.16 222.435,30.78 C220.665,29.4 218.61,28.71 216.27,28.71 C213.87,28.71 211.8,29.37 210.06,30.69 C208.32,32.01 207.09,33.87 206.37,36.27 Z"
                      />
                      <path
                        d="M247.41,65.25 L247.41,17.64 L261.99,17.64 L261.99,22.41 C265.23,18.51 269.4,16.56 274.5,16.56 C277.08,16.62 278.91,17.01 279.99,17.73 L279.99,30.42 C277.95,29.46 275.64,28.98 273.06,28.98 C270.78,28.98 268.665,29.505 266.715,30.555 C264.765,31.605 263.19,33.09 261.99,35.01 L261.99,65.25 L247.41,65.25 Z"
                      />
                      <path
                        d="M286.29,65.25 L286.29,17.64 L300.87,17.64 L300.87,20.88 C304.47,18.12 308.73,16.74 313.65,16.74 C317.37,16.74 320.655,17.55 323.505,19.17 C326.355,20.79 328.59,23.04 330.21,25.92 C331.83,28.8 332.64,32.13 332.64,35.91 L332.64,65.25 L318.06,65.25 L318.06,37.89 C318.06,35.25 317.28,33.15 315.72,31.59 C314.16,30.03 312.06,29.25 309.42,29.25 C305.76,29.25 302.91,30.51 300.87,33.03 L300.87,65.25 L286.29,65.25 Z"
                      />
                      <polygon
                        points="342 65.25 342 2.25 392.04 2.25 392.04 15.66 357.48 15.66 357.48 27.45 380.52 27.45 380.52 40.41 357.48 40.41 357.48 65.25"
                      />
                      <polygon
                        points="399.96 65.25 399.96 2.25 414.54 0 414.54 65.25"
                      />
                      <path
                        d="M429.21,84.69 C428.07,84.69 426.96,84.645 425.88,84.555 C424.8,84.465 423.9,84.33 423.18,84.15 L423.18,71.73 C424.38,71.97 425.88,72.09 427.68,72.09 C432.36,72.09 435.51,70.05 437.13,65.97 L437.13,65.88 L418.86,17.64 L434.97,17.64 L445.5,47.61 L457.74,17.64 L473.49,17.64 L452.16,67.68 C450.42,71.82 448.5,75.135 446.4,77.625 C444.3,80.115 441.87,81.915 439.11,83.025 C436.35,84.135 433.05,84.69 429.21,84.69 Z"
                      />
                    </g>
                    <g transform="translate(0.000000, 0.000000)">
                      <path
                        d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                        fill="#0066CC"
                      />
                      <path
                        d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                        fill="url(#linearGradient-compass-docked-text-expanded-mobile-expanded-example-masthead)"
                      />
                      <path
                        d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                        fill="url(#linearGradient-compass-docked-text-expanded-mobile-expanded-example-masthead)"
                        transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                      />
                    </g>
                  </g>
                </svg>
              </a>
              <a class="pf-v6-c-masthead__logo pf-m-compact" href="#">
                <svg width="37px" height="37px" viewBox="0 0 158 158">
                  <title>PatternFly</title>
                  <defs>
                    <linearGradient
                      x1="68%"
                      y1="2.25860997e-13%"
                      x2="32%"
                      y2="100%"
                      id="linearGradient-1"
                    >
                      <stop stop-color="#2B9AF3" offset="0%" />
                      <stop
                        stop-color="#73BCF7"
                        stop-opacity="0.502212631"
                        offset="100%"
                      />
                    </linearGradient>
                  </defs>
                  <g
                    id="PF-IconLogo-color"
                    stroke="none"
                    stroke-width="1"
                    fill="none"
                    fill-rule="evenodd"
                  >
                    <g id="Logo">
                      <path
                        d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                        id="Rectangle-Copy-17"
                        fill="#0066CC"
                      />
                      <path
                        d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                        id="Path-2"
                        fill="url(#linearGradient-1)"
                      />
                      <path
                        d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                        id="Path-2"
                        fill="url(#linearGradient-1)"
                        transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                      />
                    </g>
                  </g>
                </svg>
              </a>
            </div>
          </div>
          <hr class="pf-v6-c-divider" />
          <div class="pf-v6-c-masthead__content">
            <div
              class="pf-v6-c-toolbar pf-m-vertical pf-m-static"
              id="compass-docked-text-expanded-mobile-expanded-example-masthead-toolbar"
            >
              <div class="pf-v6-c-toolbar__content">
                <div class="pf-v6-c-toolbar__content-section">
                  <nav class="pf-v6-c-nav pf-m-docked" aria-label="Global">
                    <ul class="pf-v6-c-nav__list" role="list">
                      <li class="pf-v6-c-nav__item">
                        <a
                          href="#"
                          class="pf-v6-c-nav__link"
                          aria-label="Cubes"
                        >
                          <span class="pf-v6-c-nav__link-icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M12.5 12h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5v7c0 .827.673 1.5 1.5 1.5Zm.5-8h6v6h-6V4ZM5.5 25h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5v7c0 .827.673 1.5 1.5 1.5Zm.5-8h6v6H6v-6Zm24 12a1 1 0 0 1-1 1H3a1 1 0 0 1 0-2h26a1 1 0 0 1 1 1ZM18 16.5v7c0 .827.673 1.5 1.5 1.5h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5Zm2 .5h6v6h-6v-6Z"
                              />
                            </svg>
                          </span>
                          <span class="pf-v6-c-nav__link-text">System panel</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-nav__item">
                        <a
                          href="#"
                          class="pf-v6-c-nav__link pf-m-current"
                          aria-current="page"
                          aria-label="Folder"
                        >
                          <span class="pf-v6-c-nav__link-icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M29.5 8H17.81l-.681-3.208A1 1 0 0 0 16.15 4h-9.3a1 1 0 0 0-.979.792L5.19 8H2.5C1.673 8 1 8.673 1 9.5v17c0 .827.673 1.5 1.5 1.5h27c.827 0 1.5-.673 1.5-1.5v-17c0-.827-.673-1.5-1.5-1.5ZM29 26H3V10h3a1 1 0 0 0 .979-.792L7.66 6h7.682l.681 3.208a1 1 0 0 0 .979.792h12v16Z"
                              />
                            </svg>
                          </span>
                          <span class="pf-v6-c-nav__link-text">Policy</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-nav__item">
                        <a
                          href="#"
                          class="pf-v6-c-nav__link"
                          aria-label="Cloud"
                        >
                          <span class="pf-v6-c-nav__link-icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M26.996 14.228c.003-.077.004-.153.004-.228 0-4.962-4.037-9-9-9-3.899 0-7.333 2.532-8.54 6.156A6.891 6.891 0 0 0 8 11c-3.859 0-7 3.14-7 7s3.141 7 7 7h17.5c3.032 0 5.5-2.467 5.5-5.5a5.456 5.456 0 0 0-4.004-5.272ZM25.5 23H8c-2.757 0-5-2.243-5-5s2.243-5 5-5a4.97 4.97 0 0 1 1.799.34 1.003 1.003 0 0 0 1.341-.735C11.796 9.357 14.682 7 18 7c3.859 0 7 3.14 7 7 0 .311-.028.615-.067.916a1.004 1.004 0 0 0 .898 1.123 3.473 3.473 0 0 1 3.17 3.461c0 1.93-1.57 3.5-3.5 3.5Z"
                              />
                            </svg>
                          </span>
                          <span class="pf-v6-c-nav__link-text">Authentication</span>
                        </a>
                      </li>
                      <li class="pf-v6-c-nav__item">
                        <a href="#" class="pf-v6-c-nav__link" aria-label="Code">
                          <span class="pf-v6-c-nav__link-icon">
                            <svg
                              class="pf-v6-svg"
                              viewBox="0 0 32 32"
                              fill="currentColor"
                              aria-hidden="true"
                              role="img"
                              width="1em"
                              height="1em"
                            >
                              <path
                                d="M9.707 9.707 3.414 16l6.293 6.293a.999.999 0 1 1-1.414 1.414l-6.646-6.646a1.501 1.501 0 0 1 0-2.121l6.646-6.646a.999.999 0 1 1 1.414 1.414Zm20.647 5.232-6.646-6.646a.999.999 0 1 0-1.414 1.414L28.587 16l-6.293 6.293a.999.999 0 1 0 1.414 1.414l6.646-6.646a1.501 1.501 0 0 0 0-2.121ZM18.121 6.022a.997.997 0 0 0-1.186.77l-3.826 18a1 1 0 1 0 1.956.416l3.826-18a1 1 0 0 0-.77-1.186Z"
                              />
                            </svg>
                          </span>
                          <span class="pf-v6-c-nav__link-text">Network services</span>
                        </a>
                      </li>
                    </ul>
                  </nav>

                  <div
                    class="pf-v6-c-toolbar__group pf-m-align-end pf-m-spacer-none pf-m-spacer-md-on-md pf-m-action-group-plain"
                  >
                    <div class="pf-v6-c-toolbar__item">
                      <button
                        class="pf-v6-c-menu-toggle pf-m-docked pf-m-text pf-m-plain"
                        type="button"
                        aria-expanded="false"
                        aria-label="Applications"
                      >
                        <span class="pf-v6-c-menu-toggle__icon">
                          <svg
                            class="pf-v6-svg"
                            viewBox="0 0 32 32"
                            fill="currentColor"
                            aria-hidden="true"
                            role="img"
                            width="1em"
                            height="1em"
                          >
                            <path
                              d="M13.75 2H3.25C2.561 2 2 2.561 2 3.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25V3.25C15 2.561 14.439 2 13.75 2ZM13 13H4V4h9v9ZM28.75 2h-10.5C17.561 2 17 2.561 17 3.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25V3.25C30 2.561 29.439 2 28.75 2ZM28 13h-9V4h9v9Zm-14.25 4H3.25C2.561 17 2 17.561 2 18.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25v-10.5c0-.689-.561-1.25-1.25-1.25ZM13 28H4v-9h9v9Zm15.75-11h-10.5c-.689 0-1.25.561-1.25 1.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25v-10.5c0-.689-.561-1.25-1.25-1.25ZM28 28h-9v-9h9v9Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-menu-toggle__text">Applications</span>
                      </button>
                    </div>
                    <div class="pf-v6-c-toolbar__item">
                      <button
                        class="pf-v6-c-button pf-m-docked pf-m-settings pf-m-plain"
                        type="button"
                        aria-label="Settings"
                      >
                        <span class="pf-v6-c-button__icon pf-m-start">
                          <svg
                            class="pf-v6-svg"
                            viewBox="0 0 32 32"
                            fill="currentColor"
                            aria-hidden="true"
                            role="img"
                            width="1em"
                            height="1em"
                          >
                            <path
                              d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-button__text">Settings</span>
                      </button>
                    </div>
                    <div class="pf-v6-c-toolbar__item">
                      <button
                        class="pf-v6-c-menu-toggle pf-m-docked pf-m-text pf-m-plain"
                        type="button"
                        aria-expanded="false"
                        aria-label="Help"
                      >
                        <span class="pf-v6-c-menu-toggle__icon">
                          <svg
                            class="pf-v6-svg"
                            viewBox="0 0 32 32"
                            fill="currentColor"
                            aria-hidden="true"
                            role="img"
                            width="1em"
                            height="1em"
                          >
                            <path
                              d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-menu-toggle__text">Help</span>
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </header>
      </div>
    </div>
    <div class="pf-v6-c-compass__main">
      <div class="pf-v6-c-compass__main-header">
        <div class="pf-v6-c-panel pf-m-glass">
          <div class="pf-v6-c-panel__main">
            <div class="pf-v6-c-panel__main-body">
              <div class="pf-v6-c-compass__main-header-content">
                <div class="pf-v6-c-compass__main-header-title">
                  <h2 class="pf-v6-c-title pf-m-h1">Header</h2>
                </div>
                <div class="pf-v6-c-compass__main-header-toolbar">
                  <div class="pf-v6-c-action-list">
                    <div class="pf-v6-c-action-list__group">
                      <div class="pf-v6-c-action-list__item">
                        <button
                          class="pf-v6-c-button pf-m-primary"
                          type="button"
                        >
                          <span class="pf-v6-c-button__text">action</span>
                        </button>
                      </div>
                      <div class="pf-v6-c-action-list__item">
                        <button
                          class="pf-v6-c-button pf-m-secondary"
                          type="button"
                        >
                          <span class="pf-v6-c-button__text">action</span>
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-compass__content">
        <div
          class="pf-v6-c-panel pf-m-glass pf-m-scrollable-auto-height pf-m-scrollable"
        >
          <div class="pf-v6-c-panel__main">
            <div class="pf-v6-c-panel__main-body">[so much room for activities]</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

```
