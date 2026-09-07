/* /espiona-ads — extrator da Biblioteca de Anúncios da Meta.
 * Cole inteiro no javascript_tool (Claude in Chrome) com a página da Biblioteca aberta.
 * Deixa window.__ADS populado e devolve um resumo curto (não despeja as URLs: peça à parte).
 */
(() => {
  const s = [...document.querySelectorAll('script[type="application/json"]')]
    .find(x => x.textContent.includes('ad_archive_id'));
  if (!s) return JSON.stringify({ ok: false, motivo: 'Não há payload de anúncios. A página carregou? Tem captcha?', title: document.title });

  const root = JSON.parse(s.textContent);
  const ads = [];
  let total = null;

  (function walk(o) {
    if (!o || typeof o !== 'object') return;
    if (Array.isArray(o)) return o.forEach(walk);
    if (o.search_results_connection && typeof o.search_results_connection.count === 'number') {
      total = o.search_results_connection.count;
    }
    if (o.ad_archive_id && o.snapshot) {
      const sn = o.snapshot, v = (sn.videos || [])[0] || {};
      // o parâmetro efg é base64 e traz o id do asset e a duração reais
      let asset = null, dur = null;
      try {
        const efg = ((v.video_hd_url || '').match(/efg=([^&]+)/) || [])[1];
        const d = JSON.parse(atob(decodeURIComponent(efg)));
        asset = d.xpv_asset_id; dur = d.duration_s;
      } catch (e) {}
      ads.push({
        id: o.ad_archive_id,
        variantes: o.collation_count,
        ativo: o.is_active,
        ini: o.start_date ? new Date(o.start_date * 1000).toISOString().slice(0, 10) : null,
        fim: o.end_date ? new Date(o.end_date * 1000).toISOString().slice(0, 10) : null,
        plat: o.publisher_platform || [],
        page: sn.page_name, page_id: o.page_id,
        cta: sn.cta_text, cta_type: sn.cta_type, link: sn.link_url,
        titulo: sn.title, desc: sn.link_description,
        copy: (sn.body && sn.body.text) || '',
        hd: v.video_hd_url || null, sd: v.video_sd_url || null,
        poster: v.video_preview_image_url || null,
        asset, dur,
        n_img: (sn.images || []).length,
        n_cards: (sn.cards || []).length,
        cards: (sn.cards || []).map(c => ({ t: c.title, b: (c.body || '').slice(0, 80), hd: c.video_hd_url || null })),
        ia_declarada: sn.contains_digital_created_media
      });
    }
    Object.values(o).forEach(walk);
  })(root);

  const uniq = [...new Map(ads.map(a => [a.id, a])).values()];
  window.__ADS = uniq;

  // agrupa por asset pra saber quantos VÍDEOS distintos há de verdade
  const porAsset = {};
  uniq.filter(a => a.hd).forEach(a => {
    (porAsset[a.asset] = porAsset[a.asset] || { dur: a.dur, ids: [] }).ids.push(a.id);
  });

  const hoje = new Date();
  const tabela = uniq.map(a => ({
    id: a.id,
    dias: a.ini ? Math.round((hoje - new Date(a.ini)) / 864e5) : null,
    ini: a.ini,
    var: a.variantes,
    tipo: a.hd ? 'video' : (a.n_cards ? 'carrossel' : 'imagem'),
    dur: a.dur,
    cta: a.cta,
    tit: (a.titulo || '').slice(0, 50),
    hook: (a.copy || '').split('\n')[0].slice(0, 90)
  })).sort((x, y) => (y.dias || 0) - (x.dias || 0));

  return JSON.stringify({
    ok: true,
    pagina: uniq[0] && uniq[0].page,
    page_id: uniq[0] && uniq[0].page_id,
    total_na_conta: total,
    capturados: uniq.length,
    com_video: uniq.filter(a => a.hd).length,
    videos_unicos: Object.keys(porAsset).length,
    grupos_por_asset: Object.entries(porAsset)
      .filter(([, v]) => v.ids.length > 1)
      .map(([a, v]) => ({ asset: a, dur: v.dur, n: v.ids.length, ids: v.ids })),
    tabela
  }, null, 0);
})()
