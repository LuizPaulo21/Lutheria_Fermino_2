            // --- CÁLCULO DO VALOR TOTAL DO ITEM ---
            const quantidadeInput = document.getElementById('quantidade');
            const valorUnitarioInput = document.getElementById('valorUnitario');
            const valorTotalItemInput = document.getElementById('valorTotalItem');

            function calcularValorTotalItem() {
                const quantidade = parseFloat(quantidadeInput.value) || 0;
                const valorUnitario = parseFloat(valorUnitarioInput.value) || 0;
                const total = quantidade * valorUnitario;
                valorTotalItemInput.value = total.toFixed(2).replace('.', ',');
            }
            quantidadeInput.addEventListener('input', calcularValorTotalItem);
            valorUnitarioInput.addEventListener('input', calcularValorTotalItem);
            calcularValorTotalItem(); // Chama na inicialização

            // --- CONTROLE DO CAMPO PRAZO ---
            function togglePrazoConserto() {
                if (tipoConsertoRadio.checked) {
                    campoPrazoConsertoDiv.style.display = 'block';
                    prazoConsertoInput.setAttribute('required', 'required');
                } else {
                    campoPrazoConsertoDiv.style.display = 'none';
                    prazoConsertoInput.removeAttribute('required');
                    prazoConsertoInput.value = ''; // Limpa o valor se não for conserto
                }
            }
            tipoConsertoRadio.addEventListener('change', togglePrazoConserto);
            tipoCompraRadio.addEventListener('change', togglePrazoConserto);
            togglePrazoConserto(); // Chama na inicialização